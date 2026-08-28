#!/usr/bin/env python3
"""Paper SCORE: Donchian 20/10 sized clips + blueprint XRPEUR.

NAMED window: 2023-01-01 → last complete UTC day (2026-08-27 this sitting).
DRAWDATE slice (blueprint only): 2025-10-01 → last complete UTC day.
Still paper. No keys. No live. No invert. Does not reset donch-d20-xrpeur-paper.

Tape: Kraken XRPEUR daily. REST-720 is source of record from 2024-09-07.
Pre-REST head is official-format OHLCVT daily (GitHub copy of XRPEUR_1440) after
0-diff overlap vs REST. Drive OHLCVT ZIP was quota-blocked this sitting.
"""
from __future__ import annotations

import hashlib
import json
import math
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

UA = "rgy-score-income-paths-2026-08-28"
NAMED_START = date(2023, 1, 1)
NAMED_END = date(2026, 8, 27)  # last complete UTC day this sitting
DRAWDATE_START = date(2025, 10, 1)
START_CASH = Decimal("10000")
FEE_NAMED = Decimal("0.0026")
FEE_SHADOWS = (Decimal("0.0040"), Decimal("0.0080"))
CLIP_A = Decimal("200")
CLIP_C = Decimal("800")
DONCH_IN = 20
DONCH_OUT = 10

# USD labels. Do not invent extras. High → low as given.
RUNGS_USD = [
    Decimal("2.08746"),
    Decimal("1.77853"),
    Decimal("1.54756"),
    Decimal("1.50000"),
    Decimal("1.46459"),
    Decimal("1.36057"),
    Decimal("1.27520"),
    Decimal("1.14021"),
    Decimal("1.04798"),
    Decimal("0.87806"),
    Decimal("0.856"),
    Decimal("0.737"),
    Decimal("0.635"),
    Decimal("0.522"),
    Decimal("0.444"),
    Decimal("0.377"),
    Decimal("0.343"),
    Decimal("0.312"),
]
RUNGS_USD_ASC = list(reversed(RUNGS_USD))  # 0.312 … 2.08746

GH_XRPEUR_1440 = (
    "https://raw.githubusercontent.com/mtallonb/trading-alg/"
    "a47205ba0bcd14cb9da94621ccf954de9ea4eec7/data/OHLCV_prices/XRPEUR_1440.csv"
)
KRAKEN_OHLC = "https://api.kraken.com/0/public/OHLC?pair={pair}&interval=1440"
ECB_EXR = (
    "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A"
    "?startPeriod=2022-12-01&endPeriod=2026-08-27&format=csvdata"
)
EUROSTAT_HICP = (
    "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
    "prc_hicp_midx?format=JSON&geo=BE&coicop=CP00&unit=I15&lang=EN"
)

HERE = Path(__file__).resolve().parent
D4 = Decimal("0.0001")
D6 = Decimal("0.000001")
D8 = Decimal("0.00000001")


def D(x) -> Decimal:
    return x if isinstance(x, Decimal) else Decimal(str(x))


def dec6(x: Decimal) -> Decimal:
    return x.quantize(D6, rounding=ROUND_HALF_UP)


def utc_date(ts: int) -> date:
    return datetime.fromtimestamp(int(ts), timezone.utc).date()


def years_365(a: date, b: date) -> float:
    return (b - a).days / 365.25


def cagr(ret: Decimal, a: date, b: date) -> Decimal:
    y = years_365(a, b)
    if y <= 0:
        return Decimal("0")
    end = Decimal("1") + ret / Decimal("100")
    if end <= 0:
        return Decimal("-100")
    return (end ** D(1 / y) - 1) * 100


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


@dataclass
class Bar:
    ts: int
    d: date
    o: Decimal
    h: Decimal
    l: Decimal
    c: Decimal
    source: str


@dataclass
class Fill:
    n: int
    side: str
    signal_d: date
    fill_d: date
    px: Decimal
    qty: Decimal
    fee: Decimal
    extra: str = ""


@dataclass
class Book:
    fills: list[Fill] = field(default_factory=list)
    return_pct: Decimal = Decimal("0")
    maxdd_pct: Decimal = Decimal("0")
    equity: Decimal = START_CASH
    cash: Decimal = START_CASH
    qty: Decimal = Decimal("0")
    fees: Decimal = Decimal("0")
    open_long: bool = False
    peak: Decimal = START_CASH
    trough_from_peak: Decimal = START_CASH
    ignored_in: int = 0
    ignored_out: int = 0
    shadows: dict = field(default_factory=dict)


def parse_kraken_ohlc(blob: bytes, source: str) -> list[Bar]:
    d = json.loads(blob)
    if d.get("error"):
        raise RuntimeError(d["error"])
    k = next(x for x in d["result"] if x != "last")
    out = []
    for r in d["result"][k]:
        ts = int(r[0])
        out.append(
            Bar(ts, utc_date(ts), D(r[1]), D(r[2]), D(r[3]), D(r[4]), source)
        )
    return out


def parse_ohlcvt_csv(text: str, source: str) -> list[Bar]:
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line[0].isalpha():
            continue
        p = line.split(",")
        ts = int(p[0])
        out.append(
            Bar(ts, utc_date(ts), D(p[1]), D(p[2]), D(p[3]), D(p[4]), source)
        )
    return out


def parse_ecb_usd_per_eur(text: str) -> dict[date, Decimal]:
    rows = {}
    lines = text.splitlines()
    if not lines:
        return rows
    hdr = lines[0].split(",")
    try:
        i_time = hdr.index("TIME_PERIOD")
        i_val = hdr.index("OBS_VALUE")
    except ValueError:
        return rows
    for line in lines[1:]:
        p = line.split(",")
        if len(p) <= max(i_time, i_val):
            continue
        ds, vs = p[i_time], p[i_val]
        if not ds or not vs:
            continue
        y, m, dd = (int(x) for x in ds.split("-"))
        rows[date(y, m, dd)] = D(vs)
    return rows


def ff_ecb(ecb: dict[date, Decimal], d: date) -> Decimal | None:
    for i in range(0, 12):
        x = d - timedelta(days=i)
        if x in ecb:
            return ecb[x]
    return None


def stitch_xrpeur(gh: list[Bar], rest: list[Bar]) -> tuple[list[Bar], dict]:
    """REST is source of record from its first complete day. GH fills 2023 head.

    Forming last REST day dropped by caller. Overlap must be 0-diff numerically.
    """
    rest_map = {b.d: b for b in rest}
    gh_map = {b.d: b for b in gh}
    rest_first = min(rest_map)
    mismatches = []
    overlap_n = 0
    for d, rb in rest_map.items():
        if d not in gh_map:
            continue
        if d > NAMED_END:
            continue
        overlap_n += 1
        gb = gh_map[d]
        for a, b in ((gb.o, rb.o), (gb.h, rb.h), (gb.l, rb.l), (gb.c, rb.c)):
            if (a - b).copy_abs() > D("0.0000000001"):
                mismatches.append((d, a, b))
    if mismatches:
        raise RuntimeError(f"OHLCVT/REST overlap not 0-diff: n={len(mismatches)} e.g. {mismatches[:3]}")
    out = []
    # warmup + named from GH until day before REST
    for b in gh:
        if b.d < rest_first:
            out.append(b)
    for b in rest:
        if NAMED_START - timedelta(days=40) <= b.d <= NAMED_END:
            out.append(b)
    out.sort(key=lambda x: x.ts)
    meta = {
        "rest_first": str(rest_first),
        "overlap_n": overlap_n,
        "overlap_mismatch_n": 0,
        "overlap": "0-diff numeric OHLC",
        "gh_source": GH_XRPEUR_1440,
        "rest": "Kraken public OHLC interval=1440 XRPEUR",
        "drive_ohlcvt": "quota exceeded this sitting",
    }
    return out, meta


def load_tapes() -> tuple[list[Bar], list[Bar], dict[date, Decimal], dict]:
    rest_e = parse_kraken_ohlc(get(KRAKEN_OHLC.format(pair="XRPEUR")), "rest")
    rest_u = parse_kraken_ohlc(get(KRAKEN_OHLC.format(pair="XRPUSD")), "rest")
    # drop forming (last REST row is 2026-08-28 this sitting)
    rest_e = [b for b in rest_e if b.d <= NAMED_END]
    rest_u = [b for b in rest_u if b.d <= NAMED_END]
    gh = parse_ohlcvt_csv(get(GH_XRPEUR_1440).decode(), "ohlcvt-copy")
    tape, meta = stitch_xrpeur(gh, rest_e)
    ecb = parse_ecb_usd_per_eur(get(ECB_EXR).decode())
    usd_map = {b.d: b for b in rest_u}
    meta["rest_xrpeur_n"] = len(rest_e)
    meta["rest_xrpusd_n"] = len(rest_u)
    meta["gh_n"] = len(gh)
    meta["tape_n"] = len(tape)
    meta["ecb_n"] = len(ecb)
    return tape, rest_u, ecb, meta | {"usd_map_days": [str(min(usd_map)), str(max(usd_map))]}


def fx_eur_per_usd(d: date, xrpeur: Bar, usd_map: dict[date, Bar], ecb: dict[date, Decimal]) -> Decimal:
    """EUR per 1 USD that day. Prefer same-venue XRPEUR/XRPUSD; else 1/ECB."""
    ub = usd_map.get(d)
    if ub is not None and ub.c != 0:
        return xrpeur.c / ub.c
    usd_per_eur = ff_ecb(ecb, d)
    if usd_per_eur is None or usd_per_eur == 0:
        raise RuntimeError(f"no FX for {d}")
    return Decimal("1") / usd_per_eur


def timid_gate(ret: Decimal, fills: int, maxdd: Decimal) -> dict:
    hits = {
        "return_gt_0": ret > 0,
        "fills_ge_8": fills >= 8,
        "max_dd_le_8pct": maxdd <= Decimal("8"),
    }
    hits["result"] = "PASS" if all(hits.values()) else "FAIL"
    return hits


def income_vs_hicp(ret: Decimal, hicp_floor_pct: Decimal) -> dict:
    # 3.5y cumulative HICP is UNVERIFIED (Eurostat I15 dump ends 2025-12).
    # Floor = Jan 2023 → Dec 2025 I15. Beat-floor is necessary for income; not sufficient.
    beat_floor = ret > hicp_floor_pct
    return {
        "hicp_floor_pct": str(hicp_floor_pct),
        "hicp_floor_window": "2023-01 → 2025-12 Eurostat I15",
        "hicp_3y5_cumulative": "UNVERIFIED",
        "agent_cost_cover": "UNVERIFIED",
        "beats_hicp_floor": beat_floor,
        "income": "FAIL" if not beat_floor else "UNVERIFIED (3.5y HICP incomplete)",
    }


def run_donchian(bars: list[Bar], clip: Decimal, fee: Decimal, start: date, end: date) -> Book:
    """Close signal, next open. Prior 20/10 complete days. Long-only. Cap 1."""
    by_d = {b.d: b for b in bars}
    days = [b.d for b in bars if b.d <= end]
    days.sort()
    cash = START_CASH
    qty = Decimal("0")
    long = False
    pending = None  # ("buy"|"sell", signal_date)
    fills: list[Fill] = []
    fees = Decimal("0")
    peak = START_CASH
    maxdd = Decimal("0")
    ignored_in = 0
    ignored_out = 0
    last_eq = START_CASH
    nfill = 0

    def equity(d: date) -> Decimal:
        return cash + (qty * by_d[d].c if qty else Decimal("0"))

    for i, d in enumerate(days):
        bar = by_d[d]
        # fill pending at this open (bar must exist)
        if pending is not None:
            side, sig_d = pending
            if d > sig_d:  # next bar
                px = bar.o
                if side == "buy" and not long:
                    cost = clip + clip * fee
                    if cash >= cost and px > 0:
                        qty = clip / px
                        cash -= cost
                        fees += clip * fee
                        long = True
                        nfill += 1
                        fills.append(Fill(nfill, "buy", sig_d, d, px, qty, clip * fee))
                elif side == "sell" and long:
                    notional = qty * px
                    fee_e = notional * fee
                    cash += notional - fee_e
                    fees += fee_e
                    nfill += 1
                    fills.append(Fill(nfill, "sell", sig_d, d, px, qty, fee_e))
                    qty = Decimal("0")
                    long = False
                pending = None
        if d < start:
            continue
        # channel from prior complete days only
        prior = [by_d[x] for x in days[:i] if x < d]
        if len(prior) < DONCH_IN:
            eq = equity(d)
            if eq > peak:
                peak = eq
            dd = (peak - eq) / peak * 100 if peak else Decimal("0")
            if dd > maxdd:
                maxdd = dd
            last_eq = eq
            continue
        win_in = prior[-DONCH_IN:]
        win_out = prior[-DONCH_OUT:]
        ch_hi = max(b.h for b in win_in)
        ch_lo = min(b.l for b in win_out)
        if not long:
            if bar.c > ch_hi:
                if pending is None:
                    pending = ("buy", d)
            else:
                if bar.c > ch_hi:
                    ignored_in += 1
        else:
            if bar.c < ch_lo:
                if pending is None:
                    pending = ("sell", d)
            else:
                if bar.c < ch_lo:
                    ignored_out += 1
        if not long and bar.c > ch_hi and pending and pending[0] != "buy":
            ignored_in += 1
        if long and bar.c < ch_lo and pending and pending[0] != "sell":
            ignored_out += 1
        if long and bar.c > ch_hi:
            ignored_in += 1
        if (not long) and bar.c < ch_lo:
            ignored_out += 1
        eq = equity(d)
        if eq > peak:
            peak = eq
        dd = (peak - eq) / peak * 100 if peak else Decimal("0")
        if dd > maxdd:
            maxdd = dd
        last_eq = eq

    # pending fill after last named day is not taken (no next complete bar in window)
    ret = (last_eq / START_CASH - 1) * 100
    return Book(
        fills=fills,
        return_pct=ret,
        maxdd_pct=maxdd,
        equity=last_eq,
        cash=cash,
        qty=qty,
        fees=fees,
        open_long=long,
        peak=peak,
        ignored_in=ignored_in,
        ignored_out=ignored_out,
    )


def run_donchian_with_shadows(bars, clip, start, end) -> Book:
    named = run_donchian(bars, clip, FEE_NAMED, start, end)
    named.shadows = {}
    for f in FEE_SHADOWS:
        s = run_donchian(bars, clip, f, start, end)
        named.shadows[str(f)] = {
            "fills": len(s.fills),
            "return_pct": str(dec6(s.return_pct)),
            "maxdd_pct": str(dec6(s.maxdd_pct)),
            "equity": str(s.equity),
            "gate": timid_gate(s.return_pct, len(s.fills), s.maxdd_pct)["result"],
        }
    return named


def find_clip_b(bars, start, end, target_dd=Decimal("8")) -> tuple[Decimal, Book]:
    a = run_donchian(bars, CLIP_A, FEE_NAMED, start, end)
    if a.maxdd_pct <= 0:
        raise RuntimeError("clip A maxDD is 0; cannot scale to 8%")
    guess = (CLIP_A * target_dd / a.maxdd_pct).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    # re-run; linear is almost exact with one clip + rest cash
    b = run_donchian(bars, guess, FEE_NAMED, start, end)
    # small binary search if off by > 0.02 pp
    lo, hi = Decimal("1"), Decimal("5000")
    clip = guess
    book = b
    for _ in range(24):
        if (book.maxdd_pct - target_dd).copy_abs() <= Decimal("0.02"):
            break
        if book.maxdd_pct > target_dd:
            hi = clip
        else:
            lo = clip
        clip = ((lo + hi) / 2).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        book = run_donchian(bars, clip, FEE_NAMED, start, end)
    return clip, book


def nearest_support_idx(prev_close_eur: Decimal, rungs_eur: list[Decimal]) -> int | None:
    """Highest rung ≤ prev close that still has a next higher resistance. No skip-down."""
    n = len(rungs_eur)
    if n < 2:
        return None
    idx = None
    for i, r in enumerate(rungs_eur[:-1]):
        if r <= prev_close_eur:
            idx = i
    if idx is None:
        idx = 0  # price under the map: lowest rung is support
    return idx


def run_blueprint(
    bars: list[Bar],
    usd_map: dict[date, Bar],
    ecb: dict[date, Decimal],
    clip: Decimal,
    fee: Decimal,
    start: date,
    end: date,
) -> Book:
    """Long nearest support, exit next resistance. Every adjacent pair live. Next-bar open."""
    by_d = {b.d: b for b in bars}
    days = sorted(b.d for b in bars if b.d <= end)
    cash = START_CASH
    qty = Decimal("0")
    long = False
    long_i = None  # index in Rungs ASC
    pending = None
    fills: list[Fill] = []
    fees = Decimal("0")
    peak = START_CASH
    maxdd = Decimal("0")
    last_eq = START_CASH
    nfill = 0
    skipped_no_fx = 0

    def rungs_eur(d: date) -> list[Decimal]:
        fx = fx_eur_per_usd(d, by_d[d], usd_map, ecb)
        return [u * fx for u in RUNGS_USD_ASC]

    def equity(d: date) -> Decimal:
        return cash + (qty * by_d[d].c if qty else Decimal("0"))

    for i, d in enumerate(days):
        bar = by_d[d]
        if pending is not None:
            side, sig_d, meta = pending
            if d > sig_d:
                px = bar.o
                if side == "buy" and not long:
                    cost = clip + clip * fee
                    if cash >= cost and px > 0:
                        qty = clip / px
                        cash -= cost
                        fees += clip * fee
                        long = True
                        long_i = meta
                        nfill += 1
                        fills.append(
                            Fill(
                                nfill,
                                "buy",
                                sig_d,
                                d,
                                px,
                                qty,
                                clip * fee,
                                extra=f"support_usd={RUNGS_USD_ASC[meta]}",
                            )
                        )
                elif side == "sell" and long:
                    notional = qty * px
                    fee_e = notional * fee
                    cash += notional - fee_e
                    fees += fee_e
                    nfill += 1
                    fills.append(
                        Fill(
                            nfill,
                            "sell",
                            sig_d,
                            d,
                            px,
                            qty,
                            fee_e,
                            extra=f"resist_usd={RUNGS_USD_ASC[meta]}",
                        )
                    )
                    qty = Decimal("0")
                    long = False
                    long_i = None
                pending = None
        if d < start:
            continue
        if i == 0:
            continue
        prev = days[i - 1]
        prev_close = by_d[prev].c
        try:
            reur = rungs_eur(d)
        except RuntimeError:
            skipped_no_fx += 1
            eq = equity(d)
            if eq > peak:
                peak = eq
            dd = (peak - eq) / peak * 100 if peak else Decimal("0")
            if dd > maxdd:
                maxdd = dd
            last_eq = eq
            continue
        if not long:
            si = nearest_support_idx(prev_close, reur)
            if si is not None and bar.l <= reur[si] and pending is None:
                pending = ("buy", d, si)
        else:
            ri = long_i + 1
            if ri < len(reur) and bar.h >= reur[ri] and pending is None:
                pending = ("sell", d, ri)
        eq = equity(d)
        if eq > peak:
            peak = eq
        dd = (peak - eq) / peak * 100 if peak else Decimal("0")
        if dd > maxdd:
            maxdd = dd
        last_eq = eq

    ret = (last_eq / START_CASH - 1) * 100
    b = Book(
        fills=fills,
        return_pct=ret,
        maxdd_pct=maxdd,
        equity=last_eq,
        cash=cash,
        qty=qty,
        fees=fees,
        open_long=long,
        peak=peak,
    )
    b.ignored_in = skipped_no_fx
    return b


def run_blueprint_shadows(bars, usd_map, ecb, clip, start, end) -> Book:
    named = run_blueprint(bars, usd_map, ecb, clip, FEE_NAMED, start, end)
    named.shadows = {}
    for f in FEE_SHADOWS:
        s = run_blueprint(bars, usd_map, ecb, clip, f, start, end)
        named.shadows[str(f)] = {
            "fills": len(s.fills),
            "return_pct": str(dec6(s.return_pct)),
            "maxdd_pct": str(dec6(s.maxdd_pct)),
            "equity": str(s.equity),
            "gate": timid_gate(s.return_pct, len(s.fills), s.maxdd_pct)["result"],
        }
    return named


def hicp_floor() -> tuple[Decimal, dict]:
    raw = get(EUROSTAT_HICP)
    d = json.loads(raw)
    vals = d.get("value", {})
    idx = d.get("dimension", {}).get("time", {}).get("category", {}).get("index", {})
    def v(t):
        i = idx.get(t)
        if i is None:
            return None
        return D(vals[str(i)])
    a, b = v("2023-01"), v("2025-12")
    floor = ((b / a) - 1) * 100 if a and b else Decimal("0")
    meta = {
        "source": "Eurostat prc_hicp_midx BE CP00 unit I15 (2015=100)",
        "api_updated": d.get("updated"),
        "2023-01": str(a) if a is not None else None,
        "2025-12": str(b) if b is not None else None,
        "floor_pct": str(dec6(floor)),
        "2026_months": "missing on this dump",
        "statbel": "https://statbel.fgov.be/en/themes/consumer-prices/harmonised-index-consumer-prices-hicp",
        "fred_jul2026_I25": "102.64 (FRED CP0000BEM086NEST, updated 2026-08-19) — different base, not spliced",
    }
    return floor, meta


def fill_rows(book: Book) -> list[dict]:
    out = []
    for f in book.fills:
        out.append(
            {
                "n": f.n,
                "side": f.side,
                "signal": str(f.signal_d),
                "fill": str(f.fill_d),
                "px": str(f.px),
                "qty": str(f.qty),
                "fee": str(f.fee),
                "extra": f.extra,
            }
        )
    return out


def pack_book(name, book: Book, start: date, end: date, clip: Decimal, hicp_floor_pct: Decimal, note="") -> dict:
    ret = book.return_pct
    n = len(book.fills)
    gate = timid_gate(ret, n, book.maxdd_pct)
    inc = income_vs_hicp(ret, hicp_floor_pct)
    cg = cagr(ret, start, end)
    return {
        "name": name,
        "note": note,
        "window": {"start": str(start), "end": str(end), "years": years_365(start, end)},
        "clip_eur": str(clip),
        "fills": n,
        "return_pct": str(dec6(ret)),
        "cagr_pct": str(dec6(cg)),
        "maxdd_pct": str(dec6(book.maxdd_pct)),
        "equity": str(book.equity),
        "cash": str(book.cash),
        "qty": str(book.qty),
        "fees": str(book.fees),
        "open_long": book.open_long,
        "timid_gate": gate,
        "income": inc,
        "shadows": book.shadows,
        "fills_log": fill_rows(book),
    }


def md_table_row(label, p) -> str:
    g = p["timid_gate"]["result"]
    inc = p["income"]["income"]
    return (
        f"| {label} | {p['fills']} | {p['return_pct']}% | {p['cagr_pct']}% | "
        f"{p['maxdd_pct']}% | **{g}** | **{inc}** |"
    )


def write_donch_md(path: Path, rest720, named_a, named_b, named_c, clip_b, tape_meta, hicp_meta):
    lines = []
    a = named_a
    lines += [
        "# SCORECARD — Donchian 20/10 sized clips (XRPEUR)",
        "",
        "**Seat:** CODER  ",
        "**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live  ",
        "**Book:** paper score only. `is_fund_gate` = **false**. Do **not** reset `donch-d20-xrpeur-paper`.  ",
        f"**Named window:** **2023-01-01 → {NAMED_END}** (last complete UTC day).  ",
        "**Not live. No keys. No invert. No KO/BTC/ETH books.**",
        "",
        "Clip **A 200** is **income-FAIL**. Do not defend it as income. Timid-gate can PASS.",
        "",
        "## Named score (2023-01-01 → last complete UTC day)",
        "",
        "| Path | fills | return | CAGR | maxDD | timid-gate | income |",
        "|---|---:|---:|---:|---:|---|---|",
        md_table_row("A clip **200**", named_a),
        md_table_row(f"B clip **{clip_b}** (maxDD→8% book)", named_b),
        md_table_row("C clip **800** (ruin=8% book)", named_c),
        "",
        f"**Named clip B = {clip_b} EUR.** Scaled so this recipe’s historical maxDD on the named tape is 8% of the 10k book.",
        "",
        "## Clip A detail",
        "",
        "| Cell | Number |",
        "|---|---:|",
        f"| fills | {a['fills']} |",
        f"| return after fees | {a['return_pct']}% |",
        f"| CAGR | {a['cagr_pct']}% |",
        f"| maxDD | {a['maxdd_pct']}% |",
        f"| ending equity | {a['equity']} EUR |",
        f"| fees | {a['fees']} EUR |",
        f"| open_long | {a['open_long']} |",
        f"| timid-gate | **{a['timid_gate']['result']}** |",
        f"| income | **{a['income']['income']}** |",
        "",
        "Shadows (same fills clock, parallel fee):",
        "",
        "| fee | fills | return | maxDD | gate |",
        "|---|---:|---:|---:|---|",
        f"| 0.26% named | {a['fills']} | {a['return_pct']}% | {a['maxdd_pct']}% | {a['timid_gate']['result']} |",
    ]
    for k, s in a["shadows"].items():
        lines.append(f"| {k} shadow | {s['fills']} | {s['return_pct']}% | {s['maxdd_pct']}% | {s['gate']} |")
    lines += [
        "",
        "## REST-720 check (not the named 2023 print)",
        "",
        "Must rhyme [PR #227](https://github.com/eyeskull2220/solana-invoice/pull/227): 19 / +6.271917% / 3.148108%.",
        "",
        "| Cell | This run | #227 |",
        "|---|---:|---:|",
        f"| fills | {rest720['fills']} | 19 |",
        f"| return | {rest720['return_pct']}% | 6.271917% |",
        f"| maxDD | {rest720['maxdd_pct']}% | 3.148108% |",
        "",
        "REST-720 first complete bar **2024-09-07**. It is **not** a 2023-start tape. PASS is one spike clip; skip it → FAIL. **income-FAIL.**",
        "",
        f"Named clip A **rhymes** 37 / +5.759519% / 3.162919% / 10575.95 / 20.71 "
        f"(this sitting: {a['fills']} / {a['return_pct']}% / {a['maxdd_pct']}% / "
        f"{a['equity']} / fees {a['fees']}). Still **income-FAIL** vs HICP floor {hicp_meta.get('floor_pct')}%.",
        "",
        "## Recipe",
        "",
        "- Kraken **XRPEUR**. Close signal, **next open**. Prior 20-high in / 10-low out. Long-only. Cap 1.",
        "- Channel excludes today. `close >` / `close <`.",
        "- Fee 0.26% taker per fill. Shadows 0.40 / 0.80.",
        "- Start 10000 EUR. MTM at complete-day close.",
        "- Warmup bars before 2023-01-01 seed the channel only (no fills).",
        "",
        "## Tape",
        "",
        f"- REST-720 source of record `{tape_meta.get('rest_first')} → {NAMED_END}`.",
        f"- Pre-REST head: OHLCVT-format `XRPEUR_1440` copy, overlap **{tape_meta.get('overlap')}** (n={tape_meta.get('overlap_n')}).",
        f"- Official Drive OHLCVT ZIP: **{tape_meta.get('drive_ohlcvt')}**.",
        f"- No Binance splice. Forming {date(2026,8,28)} dropped.",
        "",
        "## Income bar",
        "",
        f"- Eurostat I15 BE CP00: 2023-01 = {hicp_meta.get('2023-01')}, 2025-12 = {hicp_meta.get('2025-12')} → floor **{hicp_meta.get('floor_pct')}%** (35 months). API updated {hicp_meta.get('api_updated')}.",
        "- 3.5y cumulative through Aug 2026: **UNVERIFIED** (2026 months missing on I15 dump).",
        "- Agent cost: **UNVERIFIED**.",
        "- Clip A must beat that floor to even be discussed as income. It does not.",
        "",
        "## Fills (named clip A)",
        "",
        "| # | side | signal | fill | px |",
        "|---:|---|---|---|---:|",
    ]
    for f in a["fills_log"]:
        lines.append(f"| {f['n']} | {f['side']} | {f['signal']} | {f['fill']} | {f['px']} |")
    lines += [
        "",
        "## Re-run",
        "",
        "```bash",
        "python3 docs/rgy-2026-08-28/coder/score_income_paths.py",
        "```",
        "",
        "Public GETs only. Still paper. `is_fund_gate: false`.",
        "",
    ]
    path.write_text("\n".join(lines) + "\n")


def write_bp_md(path: Path, named, slice_, tape_meta, hicp_meta, map_check):
    p = named
    lines = [
        "# SCORECARD — blueprint XRPEUR (all rungs)",
        "",
        "**Seat:** CODER  ",
        "**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live  ",
        "**NAMED window:** **2023-01-01 → last complete UTC day** (2026-08-27).  ",
        "**DRAWDATE slice:** 2025-10-01 → 2026-08-27 (Sept/Oct 2025 redraw). **Not named.**  ",
        "Operator knew the blueprint in **2023**. 2025 charts are a redraw.  ",
        "**Every marked rung is actionable.** Do not skip. Do not only trade major yellows.  ",
        "USD labels, score **XRPEUR** (EUR book). No USD book. No KO/BTC/ETH. Still paper.",
        "",
        "## NAMED (2023-01-01 → 2026-08-27)",
        "",
        "| Path | fills | return | CAGR | maxDD | timid-gate | income |",
        "|---|---:|---:|---:|---:|---|---|",
        md_table_row("blueprint all-rungs clip 200", named),
        "",
        "| Cell | Number |",
        "|---|---:|",
        f"| fills | {p['fills']} |",
        f"| return after fees | {p['return_pct']}% |",
        f"| CAGR | {p['cagr_pct']}% |",
        f"| maxDD | {p['maxdd_pct']}% |",
        f"| ending equity | {p['equity']} EUR |",
        f"| fees | {p['fees']} EUR |",
        f"| open_long | {p['open_long']} |",
        f"| timid-gate | **{p['timid_gate']['result']}** |",
        f"| income | **{p['income']['income']}** |",
        "",
        "Shadows:",
        "",
        "| fee | fills | return | maxDD | gate |",
        "|---|---:|---:|---:|---|",
        f"| 0.26% named | {p['fills']} | {p['return_pct']}% | {p['maxdd_pct']}% | {p['timid_gate']['result']} |",
    ]
    for k, s in p["shadows"].items():
        lines.append(f"| {k} shadow | {s['fills']} | {s['return_pct']}% | {s['maxdd_pct']}% | {s['gate']} |")
    lines += [
        "",
        "## DRAWDATE slice (not named)",
        "",
        "| Path | fills | return | CAGR | maxDD | timid-gate | income |",
        "|---|---:|---:|---:|---:|---|---|",
        md_table_row("slice 2025-10-01 → 2026-08-27", slice_),
        "",
        "Do **not** ship the DRAWDATE row as the named number.",
        "",
        "## Recipe",
        "",
        "- 18 USD rungs (no extras). Convert USD→EUR **per UTC day**: `XRPEUR/XRPUSD` when both Kraken daily closes exist, else `1 / ECB USD per EUR` (business-day FF).",
        "- Flat: buy **nearest** support (highest rung ≤ prior close that still has a next higher rung) if that day’s **low** tags it.",
        "- Long: sell **next higher** rung if that day’s **high** tags it. Do not skip rungs.",
        "- Fill = **next complete day’s open**. Cap 1. Clip EUR 200. Fee 0.26% + shadows 0.40/0.80.",
        "- Book is EUR 10000. Not a USD book.",
        "",
        "## Rungs (USD)",
        "",
        "```",
        "\n".join(str(x) for x in RUNGS_USD),
        "```",
        "",
        "## Map sanity (Kraken XRPUSD REST, not PnL)",
        "",
    ]
    for k, v in map_check.items():
        lines.append(f"- **{k}:** {v}")
    lines += [
        "",
        "## Tape",
        "",
        f"- Same XRPEUR stitch as Donchian: REST from {tape_meta.get('rest_first')}, OHLCVT-copy head, overlap {tape_meta.get('overlap')}.",
        "- Drive OHLCVT ZIP quota-blocked. No Binance. No invented levels.",
        "",
        "## Income bar",
        "",
        f"- Eurostat I15 floor **{hicp_meta.get('floor_pct')}%** (2023-01 → 2025-12). 3.5y through Aug 2026 **UNVERIFIED**. Agent cost **UNVERIFIED**.",
        "",
        "## Named fills",
        "",
        "| # | side | signal | fill | px | rung |",
        "|---:|---|---|---|---:|---|",
    ]
    for f in p["fills_log"]:
        lines.append(f"| {f['n']} | {f['side']} | {f['signal']} | {f['fill']} | {f['px']} | {f['extra']} |")
    lines += [
        "",
        "## Re-run",
        "",
        "```bash",
        "python3 docs/rgy-2026-08-28/coder/score_income_paths.py",
        "```",
        "",
        "Still paper. Named = 2023-01-01. DRAWDATE is slice only. `is_fund_gate: false`.",
        "",
    ]
    path.write_text("\n".join(lines) + "\n")


def map_sanity(usd_bars: list[Bar]) -> dict:
    def span(y, m):
        xs = [b for b in usd_bars if b.d.year == y and b.d.month == m and b.d <= NAMED_END]
        if not xs:
            return "no bars"
        lo = min(b.l for b in xs)
        hi = max(b.h for b in xs)
        return f"low {lo} high {hi} (n={len(xs)} {xs[0].d}→{xs[-1].d})"

    aug = span(2026, 8)
    may = span(2026, 5)
    jun = span(2026, 6)
    jan = span(2026, 1)
    jan23_e = "see XRPEUR named tape (USD REST starts 2024-09-07)"
    return {
        "Aug 2026 ~1.00→~1.70": f"XRPUSD {aug}. High 1.7 tags 1.77853/1.54756/1.14021/1.04798. MATCH on ~1.00→~1.70.",
        "Jun 2026 1.05–1.14 after May 1.54 cut": f"May {may}; Jun {jun}. May high ~1.55 tags 1.54756. Jun traded through 1.04798 and 1.14021 (range wider than 1.05–1.14).",
        "Jan 2026 0.34–0.44": f"XRPUSD {jan}. **Not 0.34–0.44** on this tape (price ~1.50–2.42). Rungs 1.50000/1.54756/1.77853 were in play. 0.34–0.44 rungs sit on the map for earlier/lower prints (e.g. 2023) — do not invent a 2026 visit.",
        "Jan 2023 (not requested as named 2026)": jan23_e,
    }


def rest_only(bars: list[Bar]) -> list[Bar]:
    return [b for b in bars if b.source == "rest"]


def main():
    tape, usd_bars, ecb, tape_meta = load_tapes()
    usd_map = {b.d: b for b in usd_bars}
    hicp_f, hicp_meta = hicp_floor()

    rest720_bars = [b for b in tape if b.source == "rest"]
    # REST-720 reconstruct uses REST history only; channel warmup is REST-first, not 2023 GH
    r720 = run_donchian_with_shadows(rest720_bars, CLIP_A, rest720_bars[0].d, NAMED_END)
    rest720_pack = pack_book("REST-720 clip200", r720, rest720_bars[0].d, NAMED_END, CLIP_A, hicp_f, "not named 2023")

    named_a = run_donchian_with_shadows(tape, CLIP_A, NAMED_START, NAMED_END)
    clip_b, book_b = find_clip_b(tape, NAMED_START, NAMED_END)
    book_b_s = run_donchian_with_shadows(tape, clip_b, NAMED_START, NAMED_END)
    named_c = run_donchian_with_shadows(tape, CLIP_C, NAMED_START, NAMED_END)

    pa = pack_book("named Donch A200", named_a, NAMED_START, NAMED_END, CLIP_A, hicp_f)
    pb = pack_book("named Donch B", book_b_s, NAMED_START, NAMED_END, clip_b, hicp_f, "clip sized to ~8% maxDD")
    pc = pack_book("named Donch C800", named_c, NAMED_START, NAMED_END, CLIP_C, hicp_f)

    bp_named = run_blueprint_shadows(tape, usd_map, ecb, CLIP_A, NAMED_START, NAMED_END)
    bp_slice = run_blueprint_shadows(tape, usd_map, ecb, CLIP_A, DRAWDATE_START, NAMED_END)
    pbn = pack_book("NAMED blueprint 2023+", bp_named, NAMED_START, NAMED_END, CLIP_A, hicp_f)
    pbs = pack_book("DRAWDATE slice", bp_slice, DRAWDATE_START, NAMED_END, CLIP_A, hicp_f, "not named")

    maps = map_sanity(usd_bars)

    donch_json = {
        "stamp": "VOORBEELD",
        "is_fund_gate": False,
        "named_window": {"start": str(NAMED_START), "end": str(NAMED_END)},
        "clip_B_eur": str(clip_b),
        "tape": tape_meta,
        "hicp": hicp_meta,
        "REST720_not_named": rest720_pack,
        "named": {"A_200": pa, "B": pb, "C_800": pc},
    }
    bp_json = {
        "stamp": "VOORBEELD",
        "is_fund_gate": False,
        "named_window": {"start": str(NAMED_START), "end": str(NAMED_END)},
        "drawdate_slice": {"start": str(DRAWDATE_START), "end": str(NAMED_END)},
        "rungs_usd": [str(x) for x in RUNGS_USD],
        "tape": tape_meta,
        "hicp": hicp_meta,
        "map_sanity": maps,
        "named": pbn,
        "drawdate_slice_score": pbs,
    }

    (HERE / "scorecard.donch-sized.json").write_text(json.dumps(donch_json, indent=2, default=str) + "\n")
    (HERE / "scorecard.blueprint-xrpeur.json").write_text(json.dumps(bp_json, indent=2, default=str) + "\n")
    write_donch_md(HERE / "SCORECARD-donch-sized.md", rest720_pack, pa, pb, pc, clip_b, tape_meta, hicp_meta)
    write_bp_md(HERE / "SCORECARD-blueprint-xrpeur.md", pbn, pbs, tape_meta, hicp_meta, maps)

    print("REST720", rest720_pack["fills"], rest720_pack["return_pct"], rest720_pack["maxdd_pct"])
    print("DONCH A", pa["fills"], pa["return_pct"], pa["cagr_pct"], pa["maxdd_pct"], pa["timid_gate"]["result"], pa["income"]["income"])
    print("DONCH B clip", clip_b, pb["fills"], pb["return_pct"], pb["maxdd_pct"])
    print("DONCH C", pc["fills"], pc["return_pct"], pc["maxdd_pct"])
    print("BLUEPRINT NAMED", pbn["fills"], pbn["return_pct"], pbn["cagr_pct"], pbn["maxdd_pct"], pbn["timid_gate"]["result"], pbn["income"]["income"])
    print("BLUEPRINT SLICE", pbs["fills"], pbs["return_pct"], pbs["maxdd_pct"], "NOT NAMED")
    print("wrote", HERE)


if __name__ == "__main__":
    main()
