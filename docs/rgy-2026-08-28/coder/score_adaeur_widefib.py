#!/usr/bin/env python3
"""Named walk-forward score for adaeur-widefib-paper.

Kraken public REST OHLC only (no API key). Venue = Kraken ADAEUR.
Named tape: interval=240 last ~720 bars (~120d), 4h wick-touch.
Shadow: interval=1440 last ~720 days, 1d wick-touch — labeled SHADOW, not the named score.

Recipe (locked):
  pair ADAEUR, clip EUR 200, cap 1 long, two prices = prior COMPLETE UTC day H and L
  arm only if (H-L)/L >= 1.04%
  flat → rest buy at L (skip if last/open would immediately cross)
  long → rest sell at H only (volume = inventory)
  after a fill, only the opposite is working; newly armed opposite does not fill this bar
  same bar both-sides → DUAL_TOUCH_SKIP (no fill either side)
  no third clip, no 14 rungs, not invert, not 15m
  fee 0.26% taker per fill, start 10000 EUR
  mark-to-market on last close for DD

Does not: invert CODE, invert-paper, dca-paper, IOTA, memecoins, live, API keys.
"""

from __future__ import annotations

import hashlib
import json
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

PAIR = "ADAEUR"
VENUE = "Kraken ADAEUR"
BOOK = "adaeur-widefib-paper"
CLIP_EUR = 200.0
FEE_RATE = 0.0026  # 0.26% taker per fill (paper engine)
START_EQUITY = 10000.0
ARM_MIN = 0.0104  # 1.04%
NAMED_INTERVAL = 240
SHADOW_INTERVAL = 1440
OHLC_LIMIT_HINT = 720
PUBLIC = "https://api.kraken.com/0/public"
UA = "adaeur-widefib-scorecard/1.0 (paper; public REST; no key)"

HERE = Path(__file__).resolve().parent
JSON_PATH = HERE / "scorecard.adaeur-widefib.json"
MD_PATH = HERE / "SCORECARD-adaeur-widefib.md"


def utc_iso(ts: int) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def utc_date(ts: int):
    return datetime.fromtimestamp(ts, timezone.utc).date()


def kraken_get(path: str) -> dict[str, Any]:
    req = urllib.request.Request(f"{PUBLIC}/{path}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
    body = json.loads(raw.decode())
    if body.get("error"):
        raise RuntimeError(f"Kraken {path} error: {body['error']}")
    return body


def fetch_ohlc(interval: int) -> tuple[str, list[list[Any]], int, str]:
    body = kraken_get(f"OHLC?pair={PAIR}&interval={interval}")
    result = body["result"]
    key = next(k for k in result if k != "last")
    rows = result[key]
    blob = json.dumps(rows, separators=(",", ":")).encode()
    digest = hashlib.sha256(blob).hexdigest()
    return key, rows, int(result["last"]), digest


def parse_bars(rows: list[list[Any]], drop_forming: bool = True) -> list[dict[str, Any]]:
    bars: list[dict[str, Any]] = []
    for row in rows:
        ts = int(row[0])
        o, h, l, c = (float(row[1]), float(row[2]), float(row[3]), float(row[4]))
        bars.append(
            {
                "ts": ts,
                "iso": utc_iso(ts),
                "date": utc_date(ts),
                "open": o,
                "high": h,
                "low": l,
                "close": c,
            }
        )
    if drop_forming and len(bars) >= 2:
        # Forming bar: last row is the unclosed bucket (Kraken OHLC convention).
        bars = bars[:-1]
    return bars


def daily_rails(daily_closed: list[dict[str, Any]]) -> dict[Any, dict[str, float]]:
    """Map calendar date → that UTC day's H/L (complete 1d bar only)."""
    out: dict[Any, dict[str, float]] = {}
    for b in daily_closed:
        out[b["date"]] = {"H": b["high"], "L": b["low"], "C": b["close"]}
    return out


def prior_rails(rails: dict[Any, dict[str, float]], day) -> dict[str, float] | None:
    return rails.get(day - timedelta(days=1))


def mtm_equity(cash: float, qty: float, last: float) -> float:
    return cash + qty * last


def walk_forward(
    bars: list[dict[str, Any]],
    rails: dict[Any, dict[str, float]],
    tape_name: str,
) -> dict[str, Any]:
    """Causal two-price ping-pong. At most one resting limit. Cap 1 long."""
    cash = START_EQUITY
    qty = 0.0
    state = "FLAT"  # FLAT | LONG
    pair_l: float | None = None
    pair_h: float | None = None
    working: str | None = None  # "buy" | "sell" | None
    peak = START_EQUITY
    max_dd = 0.0
    fees = 0.0
    fills: list[dict[str, Any]] = []
    n_dual = 0
    n_cross = 0
    n_buy = 0
    n_sell = 0
    days_seen: set[Any] = set()
    days_armed: set[Any] = set()
    days_skipped: set[Any] = set()

    def mark(close: float) -> float:
        nonlocal peak, max_dd
        eq = mtm_equity(cash, qty, close)
        if eq > peak:
            peak = eq
        dd = (peak - eq) / peak if peak > 0 else 0.0
        if dd > max_dd:
            max_dd = dd
        return eq

    for i, bar in enumerate(bars):
        prev_close = bars[i - 1]["close"] if i else bar["open"]
        day = bar["date"]
        days_seen.add(day)
        prior = prior_rails(rails, day)
        range_ok = False
        cand_l = cand_h = None
        if prior and prior["L"] > 0:
            cand_l, cand_h = prior["L"], prior["H"]
            range_ok = (cand_h - cand_l) / cand_l >= ARM_MIN
        if range_ok:
            days_armed.add(day)
        else:
            days_skipped.add(day)

        # Flat: cancel unfilled buy and re-decide from *this* bar's prior complete day.
        # Long: freeze the pair we bought; rest sell at that H only (no third clip).
        if state == "FLAT":
            working = None
            pair_l = pair_h = None
            if range_ok:
                assert cand_l is not None and cand_h is not None
                # Immediate-cross skip: a buy LIMIT at L is marketable if last/open
                # is already <= L (operator skip: last 0.17451 < L 0.178212).
                if bar["open"] <= cand_l or prev_close <= cand_l:
                    n_cross += 1
                else:
                    pair_l, pair_h = cand_l, cand_h
                    working = "buy"
        elif state == "LONG" and working is None:
            # Newly armed opposite is eligible from this bar (the bar after the buy).
            working = "sell"

        dual = False
        if (
            working is not None
            and pair_l is not None
            and pair_h is not None
            and bar["low"] <= pair_l
            and bar["high"] >= pair_h
        ):
            # OHLC has no path. Do not credit a round-trip inside one bar.
            dual = True
            n_dual += 1

        if not dual and working == "buy" and pair_l is not None:
            if bar["low"] <= pair_l:
                fill_px = pair_l
                lot = CLIP_EUR / fill_px
                fee = CLIP_EUR * FEE_RATE
                cash -= CLIP_EUR + fee
                fees += fee
                qty = lot
                state = "LONG"
                working = None  # sell rests from the next bar only
                n_buy += 1
                fills.append(
                    {
                        "i": len(fills) + 1,
                        "side": "buy",
                        "price": fill_px,
                        "qty": lot,
                        "fee_eur": fee,
                        "bar_iso": bar["iso"],
                        "pair_L": pair_l,
                        "pair_H": pair_h,
                    }
                )
        elif not dual and working == "sell" and pair_h is not None and qty > 0:
            if bar["high"] >= pair_h:
                fill_px = pair_h
                notional = qty * fill_px
                fee = notional * FEE_RATE
                cash += notional - fee
                fees += fee
                fills.append(
                    {
                        "i": len(fills) + 1,
                        "side": "sell",
                        "price": fill_px,
                        "qty": qty,
                        "fee_eur": fee,
                        "bar_iso": bar["iso"],
                        "pair_L": pair_l,
                        "pair_H": pair_h,
                    }
                )
                qty = 0.0
                state = "FLAT"
                working = None
                pair_l = pair_h = None
                n_sell += 1

        mark(bar["close"])

    last_close = bars[-1]["close"] if bars else 0.0
    ending = mtm_equity(cash, qty, last_close)
    ret_pct = (ending - START_EQUITY) / START_EQUITY * 100.0
    max_dd_pct = max_dd * 100.0
    n_fills = n_buy + n_sell
    n_closed = n_sell
    g_ret = ret_pct > 0
    g_fills = n_fills >= 8
    g_dd = max_dd_pct <= 8.0
    gate = "PASS" if (g_ret and g_fills and g_dd) else "FAIL"

    open_note: dict[str, Any] | None = None
    if state == "LONG" and fills:
        entry = fills[-1]
        max_hi = 0.0
        n_after = 0
        for b in bars:
            if b["iso"] <= entry["bar_iso"]:
                continue
            n_after += 1
            if b["high"] > max_hi:
                max_hi = b["high"]
        open_note = {
            "entry_iso": entry["bar_iso"],
            "pair_L": entry["pair_L"],
            "pair_H": entry["pair_H"],
            "bars_after_entry": n_after,
            "max_high_after_entry": max_hi,
            "sell_tagged": bool(entry["pair_H"] is not None and max_hi >= entry["pair_H"]),
        }

    return {
        "tape": tape_name,
        "n_bars_scored": len(bars),
        "window_start": bars[0]["iso"] if bars else None,
        "window_end": bars[-1]["iso"] if bars else None,
        "fills": n_fills,
        "n_buy_fills": n_buy,
        "n_sell_fills": n_sell,
        "n_closed_pairs": n_closed,
        "n_dual_touch_skips": n_dual,
        "n_cross_skips": n_cross,
        "days_in_window": len(days_seen),
        "days_armed": len(days_armed),
        "days_skipped": len(days_skipped),
        "start_equity_eur": START_EQUITY,
        "ending_equity_eur": ending,
        "ending_cash_eur": cash,
        "ending_qty": qty,
        "ending_state": state,
        "ending_mark": last_close,
        "fees_eur": fees,
        "return_after_fees_pct": ret_pct,
        "max_dd_pct": max_dd_pct,
        "peak_equity_eur": peak,
        "open_inventory": open_note,
        "gate": {
            "return_gt_0": g_ret,
            "fills_ge_8": g_fills,
            "max_dd_le_8pct": g_dd,
            "result": gate,
        },
        "fills_log": fills,
    }


def round_num(x: float, n: int = 6) -> float:
    return round(float(x), n)


def compact_score(s: dict[str, Any]) -> dict[str, Any]:
    out = dict(s)
    out["ending_equity_eur"] = round_num(s["ending_equity_eur"], 8)
    out["ending_cash_eur"] = round_num(s["ending_cash_eur"], 8)
    out["ending_qty"] = round_num(s["ending_qty"], 10)
    out["fees_eur"] = round_num(s["fees_eur"], 8)
    out["return_after_fees_pct"] = round_num(s["return_after_fees_pct"], 6)
    out["max_dd_pct"] = round_num(s["max_dd_pct"], 6)
    out["peak_equity_eur"] = round_num(s["peak_equity_eur"], 8)
    if s.get("open_inventory"):
        oi = dict(s["open_inventory"])
        oi["pair_L"] = round_num(oi["pair_L"], 8) if oi["pair_L"] is not None else None
        oi["pair_H"] = round_num(oi["pair_H"], 8) if oi["pair_H"] is not None else None
        oi["max_high_after_entry"] = round_num(oi["max_high_after_entry"], 8)
        out["open_inventory"] = oi
    log = []
    for f in s["fills_log"]:
        log.append(
            {
                **f,
                "price": round_num(f["price"], 8),
                "qty": round_num(f["qty"], 10),
                "fee_eur": round_num(f["fee_eur"], 8),
                "pair_L": round_num(f["pair_L"], 8) if f["pair_L"] is not None else None,
                "pair_H": round_num(f["pair_H"], 8) if f["pair_H"] is not None else None,
            }
        )
    out["fills_log"] = log
    return out


def render_md(payload: dict[str, Any]) -> str:
    n = payload["named_score"]
    sh = payload["shadow_1d"]
    g = n["gate"]["result"]
    conjuncts = n["gate"]
    tape = payload["named_tape"]
    lines = [
        f"# SCORECARD — `{BOOK}`",
        "",
        f"**Seat:** CODER  ",
        f"**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live  ",
        f"**Book:** `{BOOK}` (new paper book). `is_fund_gate` = **{str(payload['is_fund_gate']).lower()}** on **this book only** — not `invert-paper`.  ",
        f"**Fetched:** {payload['fetched_at_utc']}",
        "",
        f"## Gate: **{g}**",
        "",
        "All three conjuncts (named 4h tape, after 0.26% taker, no invented fills):",
        "",
        "| Conjunct | Value | Need | Hit |",
        "|---|---:|---|---|",
        f"| return after fees | **{n['return_after_fees_pct']:.6f}%** | > 0 | {'YES' if conjuncts['return_gt_0'] else 'NO'} |",
        f"| fills | **{n['fills']}** | ≥ 8 | {'YES' if conjuncts['fills_ge_8'] else 'NO'} |",
        f"| max DD (MTM last close) | **{n['max_dd_pct']:.6f}%** | ≤ 8% | {'YES' if conjuncts['max_dd_le_8pct'] else 'NO'} |",
        f"| **result** | | | **{g}** |",
        "",
        "## Named score (4h wick-touch)",
        "",
        "| Cell | Number |",
        "|---|---:|",
        f"| fills | {n['fills']} |",
        f"| buy fills | {n['n_buy_fills']} |",
        f"| sell fills | {n['n_sell_fills']} |",
        f"| n closed pairs | {n['n_closed_pairs']} |",
        f"| dual-skips (`DUAL_TOUCH_SKIP`) | {n['n_dual_touch_skips']} |",
        f"| immediate-cross skips (buy rest) | {n['n_cross_skips']} |",
        f"| days armed (`(H−L)/L ≥ 1.04%`) | {n['days_armed']} |",
        f"| days skipped (range < 1.04%) | {n['days_skipped']} |",
        f"| days in window | {n['days_in_window']} |",
        f"| return after fees % | {n['return_after_fees_pct']:.6f} |",
        f"| max DD % | {n['max_dd_pct']:.6f} |",
        f"| start equity EUR | {n['start_equity_eur']:.2f} |",
        f"| ending equity EUR (MTM) | {n['ending_equity_eur']:.8f} |",
        f"| ending cash EUR | {n['ending_cash_eur']:.8f} |",
        f"| ending qty ADA | {n['ending_qty']:.10f} |",
        f"| ending state | {n['ending_state']} |",
        f"| fees EUR | {n['fees_eur']:.8f} |",
        "",
        "Named fills (limit price, 4h wick-touch, Kraken ADAEUR):",
        "",
        "| # | side | price | bar UTC | pair L / H |",
        "|---:|---|---:|---|---|",
    ]
    for f in n["fills_log"]:
        lines.append(
            f"| {f['i']} | {f['side']} | {f['price']:.8f} | `{f['bar_iso']}` | {f['pair_L']:.8f} / {f['pair_H']:.8f} |"
        )
    oi = n.get("open_inventory")
    if oi:
        tagged = "tagged" if oi["sell_tagged"] else "never tagged"
        lines += [
            "",
            f"Open clip: LONG from `{oi['entry_iso']}` sell resting at **{oi['pair_H']:.8f}**. "
            f"Max later 4h high **{oi['max_high_after_entry']:.8f}** ({tagged}; {oi['bars_after_entry']} bars). "
            "No invented fill.",
        ]
    lines += [
        "",
        "## Tape (named)",
        "",
        "| | |",
        "|---|---|",
        f"| venue | **{payload['venue']}** (no Binance splice) |",
        f"| pair | `{PAIR}` |",
        f"| interval | {tape['interval']} (4h) |",
        f"| fetched rows | {tape['n_bars_fetched']} |",
        f"| scored closed bars | {tape['n_bars_scored']} (forming bar dropped) |",
        f"| window | `{tape['window_start']}` → `{tape['window_end']}` UTC |",
        f"| daily rails | interval=1440 complete bars `{payload['daily_rails']['first']}` → `{payload['daily_rails']['last_complete']}` |",
        f"| OHLC sha256 (4h fetched) | `{tape['sha256']}` |",
        "",
        "## Recipe (what was scored)",
        "",
        "- Two prices only: prior **complete UTC day** H and L. No lookahead (today’s 1d bar is invisible).",
        "- Arm only if `(H−L)/L ≥ 1.04%`. Else skip the day.",
        "- If flat: rest **buy at L**. Skip the rest if last/open would immediately cross (`open ≤ L` or `prev_close ≤ L`).",
        "- If long: rest **sell at H only**, volume = inventory. Cap **1** long. No third clip.",
        "- After a fill, only the opposite is working. Newly armed opposite does **not** fill the fill bar.",
        "- Fill = 4h wick-touch at the limit (`low ≤ L` buy, `high ≥ H` sell). Fill price = the limit, not the wick.",
        "- Same 4h bar both-sides: **`DUAL_TOUCH_SKIP`** — no fill either side.",
        "- Fee **0.26% taker per fill**. Clip **EUR 200**. Start **10000 EUR**.",
        "- Max DD: mark-to-market on each scored bar’s **close**.",
        "- **Not** invert. **Not** 14 rungs. **Not** 15m. **Not** `invert-paper`. **Not** `dca-paper`.",
        "",
        "## SHADOW — 1d wick-touch (not the named score)",
        "",
        "Same recipe, fill clock = Kraken `interval=1440` last ~720 **days**. Do not mix into the named cells.",
        "",
        "| Cell | SHADOW |",
        "|---|---:|",
        f"| window | `{sh['window_start']}` → `{sh['window_end']}` |",
        f"| scored closed days | {sh['n_bars_scored']} |",
        f"| fills | {sh['fills']} |",
        f"| n closed pairs | {sh['n_closed_pairs']} |",
        f"| dual-skips | {sh['n_dual_touch_skips']} |",
        f"| cross-skips | {sh['n_cross_skips']} |",
        f"| days armed / skipped | {sh['days_armed']} / {sh['days_skipped']} |",
        f"| return after fees % | {sh['return_after_fees_pct']:.6f} |",
        f"| max DD % | {sh['max_dd_pct']:.6f} |",
        f"| ending equity EUR | {sh['ending_equity_eur']:.8f} |",
        f"| shadow gate (informational) | {sh['gate']['result']} |",
        "",
        "## Operator box (cite, do not ping)",
        "",
        f"- `{BOOK}` created **2026-08-28 21:59 Europe/Brussels**, EUR 10000, fee 0.26%, allow ADAEUR only.",
        "- Empty: **0 fills, 0 orders**. This VM did **not** run Kraken paper CLI against that box.",
        "- Live resters were **SKIPPED** because last **0.17451** is already below prior-day L **0.178212** (a buy at L would cross). This score uses the same cross-skip rule.",
        "- `invert-paper` and `dca-paper` were **not** touched. No reset. No invert CODE. No IOTA. No memecoins. No live. No API keys.",
        "",
        "## Re-run",
        "",
        "```bash",
        "python3 docs/rgy-2026-08-28/coder/score_adaeur_widefib.py",
        "```",
        "",
        "Public GETs only. Writes this markdown and `scorecard.adaeur-widefib.json`.",
        "",
        f"**{g}.** Still paper.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ticker = kraken_get(f"Ticker?pair={PAIR}")["result"]
    tick_key = next(iter(ticker))
    last_px = float(ticker[tick_key]["c"][0])

    dkey, drows, dlast, dsha = fetch_ohlc(SHADOW_INTERVAL)
    hkey, hrows, hlast, hsha = fetch_ohlc(NAMED_INTERVAL)
    if dkey != PAIR or hkey != PAIR:
        raise RuntimeError(f"unexpected pair keys: {dkey!r} {hkey!r}")

    daily_closed = parse_bars(drows, drop_forming=True)
    h4_closed = parse_bars(hrows, drop_forming=True)
    rails = daily_rails(daily_closed)

    named = compact_score(walk_forward(h4_closed, rails, "named_4h"))
    shadow = compact_score(walk_forward(daily_closed, rails, "shadow_1d"))

    is_fund = named["gate"]["result"] == "PASS"

    payload = {
        "book": BOOK,
        "is_fund_gate": is_fund,
        "is_fund_gate_note": "this NEW book only; not invert-paper; not dca-paper",
        "still_paper": True,
        "venue": VENUE,
        "pair": PAIR,
        "fetched_at_utc": fetched_at,
        "ticker_last": last_px,
        "recipe": {
            "clip_eur": CLIP_EUR,
            "cap_long": 1,
            "prices": "prior_complete_utc_day_H_and_L",
            "arm_min_range_frac": ARM_MIN,
            "fee_taker_per_fill": FEE_RATE,
            "start_equity_eur": START_EQUITY,
            "fill_model_named": "4h_wick_touch",
            "dual_touch": "DUAL_TOUCH_SKIP",
            "cross_skip_buy": "skip rest if open<=L or prev_close<=L",
            "not": ["invert", "14_rungs", "15m", "third_clip", "binance_splice"],
        },
        "named_tape": {
            "interval": NAMED_INTERVAL,
            "interval_name": "4h",
            "n_bars_fetched": len(hrows),
            "n_bars_scored": named["n_bars_scored"],
            "window_start": named["window_start"],
            "window_end": named["window_end"],
            "forming_bar_dropped": True,
            "api_last": hlast,
            "sha256": hsha,
            "hint": f"last ~{OHLC_LIMIT_HINT} bars is the NAMED tape (~120d)",
        },
        "daily_rails": {
            "interval": SHADOW_INTERVAL,
            "n_bars_fetched": len(drows),
            "n_complete": len(daily_closed),
            "first": daily_closed[0]["iso"] if daily_closed else None,
            "last_complete": daily_closed[-1]["iso"] if daily_closed else None,
            "forming_bar_dropped": True,
            "sha256": dsha,
        },
        "named_score": named,
        "shadow_1d": {
            **shadow,
            "label": "SHADOW",
            "interval": SHADOW_INTERVAL,
            "interval_name": "1d",
            "n_bars_fetched": len(drows),
            "sha256": dsha,
            "note": "1d-touch shadow on interval=1440 last ~720 days. Not the named score.",
        },
        "operator_box": {
            "name": BOOK,
            "created": "2026-08-28 21:59 Europe/Brussels",
            "equity_eur": 10000,
            "fee": "0.26%",
            "allow": "ADAEUR only",
            "fills": 0,
            "orders": 0,
            "live_resters": "SKIPPED — last 0.17451 already below prior-day L 0.178212",
            "invert_paper": "not touched",
            "dca_paper": "not touched",
            "this_vm": "did not use Kraken paper CLI",
        },
        "script": "docs/rgy-2026-08-28/coder/score_adaeur_widefib.py",
    }

    JSON_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    MD_PATH.write_text(render_md(payload), encoding="utf-8")

    n = named
    print("=== NAMED SCORE adaeur-widefib-paper (4h wick-touch, Kraken ADAEUR) ===")
    print(f"tape     {n['window_start']} -> {n['window_end']}  bars={n['n_bars_scored']}")
    print(f"fills    {n['fills']}  closed_pairs={n['n_closed_pairs']}  dual_skips={n['n_dual_touch_skips']}  cross_skips={n['n_cross_skips']}")
    print(f"days     armed={n['days_armed']} skipped={n['days_skipped']} window={n['days_in_window']}")
    print(f"return   {n['return_after_fees_pct']:.6f}%   maxDD={n['max_dd_pct']:.6f}%")
    print(f"equity   {n['ending_equity_eur']:.8f} EUR  (start {START_EQUITY:.2f})")
    print(f"GATE     {n['gate']['result']}  return>0={n['gate']['return_gt_0']} fills>=8={n['gate']['fills_ge_8']} dd<=8%={n['gate']['max_dd_le_8pct']}")
    print(f"is_fund_gate (this book only) {str(is_fund).lower()}")
    print("--- SHADOW 1d (not named) ---")
    print(f"fills={shadow['fills']} closed={shadow['n_closed_pairs']} dual={shadow['n_dual_touch_skips']} ret={shadow['return_after_fees_pct']:.6f}% dd={shadow['max_dd_pct']:.6f}% {shadow['gate']['result']}")
    print(f"wrote {JSON_PATH}")
    print(f"wrote {MD_PATH}")


if __name__ == "__main__":
    main()
