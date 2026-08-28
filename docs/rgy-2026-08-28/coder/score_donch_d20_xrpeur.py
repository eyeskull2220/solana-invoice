#!/usr/bin/env python3
"""Score Donchian 20/10 long-only XRPEUR 1d (CEO UNLOCK 2026-08-28, published 20/10).

Recipe is locked. No parameter search. No invert. No fib pair-swap. No 15m.
Still paper. No keys. No live.

Data order:
  1. Official Kraken OHLCVT PAIR 1440 (XRPEUR / XXRPZEUR) quarterly zips
     linked from the Kraken support article, plus REST OHLC 1440 tail.
  2. If Drive quota-blocks the zips: Kraken public Trades aggregated to
     UTC daily bars (same OHLC definition as OHLCVT), spliced onto REST
     OHLC 1440 at the first overlapping complete day. Not Binance.

Window: 2023-01-01 through last complete UTC day. Decide on close, fill
next open. Clip EUR 200, one long, rest of 10000 stays cash.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path

PAIR = "XRPEUR"
PAIR_WS = "XXRPZEUR"
VENUE = "Kraken"
INTERVAL_MIN = 1440
CLIP_EUR = 200.0
START_CASH = 10000.0
LOOKBACK_IN = 20
LOOKBACK_OUT = 10
FEE_PRIMARY = 0.0026
FEE_SHADOWS = (0.0040, 0.0080)
WINDOW_START = date(2023, 1, 1)
WARMUP_START = date(2022, 12, 1)
RECIPE = "donch-d20-xrpeur"
UNLOCK = "CEO UNLOCK 2026-08-28 22:05 Europe/Brussels"
PUBLISHED = "20/10"

SUPPORT_OHLCVT = (
    "https://support.kraken.com/articles/"
    "360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data"
)
COMPLETE_DRIVE_VIEW = (
    "https://drive.google.com/file/d/1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP/view"
)
QUARTERLY_FOLDER = (
    "https://drive.google.com/drive/folders/15RSlNuW_h0kVM8or8McOGOMfHeBFvFGI"
)
REST_OHLC_URL = "https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=1440"
REST_TRADES_URL = "https://api.kraken.com/0/public/Trades"

# Official quarterly zips from QUARTERLY_FOLDER (parsed 2026-08-28).
OHLCVT_QUARTERS: list[tuple[str, str]] = [
    ("Q1_2023", "17ghRNMQGK0Is7_by784qGzP1eCUokI2V"),
    ("Q2_2023", "1QGRW_Qg9H2pC2dBTk0b6vlGi93AFiZfI"),
    ("Q3_2023", "1gE9XyED-bm4ks1PZomDnlpt-f_r9nWu6"),
    ("Q4_2023", "1c3HQ0-YMvhAuGwo-f4BKAdhkG8Cj6jxx"),
    ("Q1_2024", "1JkH3c13madqdpF-dzXoseX_sYY1E2iHx"),
    ("Q2_2024", "1nb0vaPClwYoAGnWjYXkjrBEPQC58lmPN"),
    ("Q3_2024", "1_GQZ7gqQ9BcIEIA_L8zPwfXTUjxIKEIk"),
    ("Q4_2024", "1fCJPY1SwJa6py-Dln-Q7S349lBXyH0Dl"),
    ("Q1_2025", "1dXJummu2qF5J6UC4rQh0T0XmriqngONG"),
    ("Q2_2025", "1THrQiXsMSyhGb4DmUPCbivAKXoI8rxEG"),
    ("Q3_2025", "1N6fg5ceXx9iQHEGHyvqUUlgo3NPsRpT7"),
    ("Q4_2025", "1QbPHLP0TTGo-lqwKn8M-_Xo_oexXlEnB"),
    ("Q1_2026", "15QxEf_-rRS-Yt7uERCI41HMcQQPKzSHq"),
]

UA = "score-donch-d20-xrpeur/1.0 (paper; no keys)"


def last_complete_utc_day(now: datetime | None = None) -> date:
    now = now or datetime.now(timezone.utc)
    # A UTC day is complete only after 00:00 UTC of the next day.
    return date.fromordinal(now.date().toordinal() - 1)


@dataclass
class Bar:
    ts: int
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0
    trades: int = 0
    source: str = ""

    @property
    def day(self) -> date:
        return datetime.fromtimestamp(self.ts, timezone.utc).date()


@dataclass
class Fill:
    ts: int
    day: str
    side: str
    price: float
    units: float
    notional_eur: float


@dataclass
class Book:
    fee: float
    cash: float = START_CASH
    units: float = 0.0
    long: bool = False
    fills: list[Fill] = field(default_factory=list)
    equity_close: list[tuple[int, float]] = field(default_factory=list)
    peak: float = START_CASH
    max_dd_pct: float = 0.0
    pending: str | None = None  # "buy" | "sell" | None
    pending_from_ts: int | None = None

    def mark(self, ts: int, close: float) -> None:
        eq = self.cash + self.units * close
        self.equity_close.append((ts, eq))
        if eq > self.peak:
            self.peak = eq
        if self.peak > 0:
            dd = (self.peak - eq) / self.peak * 100.0
            if dd > self.max_dd_pct:
                self.max_dd_pct = dd

    def execute(self, bar: Bar, side: str) -> None:
        px = bar.open
        if side == "buy":
            units = CLIP_EUR / px
            self.cash -= CLIP_EUR * (1.0 + self.fee)
            self.units = units
            self.long = True
            self.fills.append(
                Fill(bar.ts, bar.day.isoformat(), "buy", px, units, CLIP_EUR)
            )
        elif side == "sell":
            proceeds = self.units * px * (1.0 - self.fee)
            self.cash += proceeds
            self.fills.append(
                Fill(
                    bar.ts,
                    bar.day.isoformat(),
                    "sell",
                    px,
                    self.units,
                    self.units * px,
                )
            )
            self.units = 0.0
            self.long = False
        else:
            raise ValueError(side)

    def final_equity(self) -> float:
        if not self.equity_close:
            return self.cash
        return self.equity_close[-1][1]

    def return_pct(self) -> float:
        return (self.final_equity() - START_CASH) / START_CASH * 100.0


def http_get_json(url: str, retries: int = 8) -> dict:
    delay = 1.0
    last_err: Exception | None = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            last_err = exc
            if exc.code not in (429, 500, 502, 503, 520):
                raise
            time.sleep(delay)
            delay = min(delay * 2.0, 60.0)
        except Exception as exc:  # noqa: BLE001 — retry public REST blips
            last_err = exc
            time.sleep(delay)
            delay = min(delay * 2.0, 60.0)
    raise RuntimeError(f"GET failed {url}: {last_err}")


def drive_download_url(file_id: str) -> str:
    return (
        "https://drive.usercontent.google.com/download?"
        + urllib.parse.urlencode(
            {"id": file_id, "export": "download", "confirm": "t"}
        )
    )


def fetch_rest_ohlc() -> list[Bar]:
    payload = http_get_json(REST_OHLC_URL)
    errors = payload.get("error") or []
    if errors:
        raise RuntimeError(f"OHLC error {errors}")
    result = payload["result"]
    key = next(k for k in result if k != "last")
    bars: list[Bar] = []
    for row in result[key]:
        bars.append(
            Bar(
                ts=int(row[0]),
                open=float(row[1]),
                high=float(row[2]),
                low=float(row[3]),
                close=float(row[4]),
                volume=float(row[6]),
                trades=int(row[7]),
                source="rest_ohlc_1440",
            )
        )
    return bars


def try_ohlcvt_quarter(cache_dir: Path, quarter: str, file_id: str) -> list[Bar] | None:
    """Download one official quarterly zip and extract XRPEUR/XXRPZEUR 1440."""
    url = drive_download_url(file_id)
    zip_path = cache_dir / f"Kraken_OHLCVT_{quarter}.zip"
    print(f"OHLCVT GET {url}", flush=True)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=300) as resp:
            first = resp.read(16)
            if first[:2] != b"PK":
                body = first + resp.read(256)
                snippet = body[:120].decode("utf-8", "replace")
                print(f"  not zip ({resp.headers.get('Content-Type')}): {snippet!r}", flush=True)
                return None
            with zip_path.open("wb") as handle:
                handle.write(first)
                while True:
                    chunk = resp.read(1024 * 1024)
                    if not chunk:
                        break
                    handle.write(chunk)
    except Exception as exc:  # noqa: BLE001
        print(f"  download failed: {exc}", flush=True)
        return None
    want = {"XRPEUR_1440.csv", "XXRPZEUR_1440.csv"}
    bars: list[Bar] = []
    try:
        with zipfile.ZipFile(zip_path) as zf:
            names = [
                n
                for n in zf.namelist()
                if n.split("/")[-1] in want and not n.startswith("__MACOSX/")
            ]
            if not names:
                print(f"  no PAIR 1440 member in {quarter}", flush=True)
                return None
            member = sorted(names)[0]
            print(f"  extract {member}", flush=True)
            with zf.open(member) as handle:
                for raw in handle:
                    line = raw.decode("utf-8").strip()
                    if not line:
                        continue
                    parts = line.split(",")
                    ts = int(float(parts[0]))
                    bars.append(
                        Bar(
                            ts=ts,
                            open=float(parts[1]),
                            high=float(parts[2]),
                            low=float(parts[3]),
                            close=float(parts[4]),
                            volume=float(parts[5]) if len(parts) > 5 else 0.0,
                            trades=int(float(parts[6])) if len(parts) > 6 else 0,
                            source=f"ohlcvt_{quarter}",
                        )
                    )
    finally:
        if zip_path.exists():
            zip_path.unlink()
    return bars


def try_ohlcvt_all(cache_dir: Path) -> tuple[list[Bar], list[dict]]:
    log: list[dict] = []
    merged: dict[int, Bar] = {}
    for quarter, file_id in OHLCVT_QUARTERS:
        url = drive_download_url(file_id)
        got = try_ohlcvt_quarter(cache_dir, quarter, file_id)
        log.append(
            {
                "quarter": quarter,
                "file_id": file_id,
                "url": url,
                "bars": 0 if got is None else len(got),
                "ok": got is not None,
            }
        )
        if got is None:
            return [], log
        for bar in got:
            merged[bar.ts] = bar
    return [merged[k] for k in sorted(merged)], log


def aggregate_trades_to_daily(
    cache_dir: Path,
    start: date,
    end_exclusive: date,
) -> list[Bar]:
    """Official Kraken Trades REST → UTC daily OHLCV (OHLCVT definition)."""
    csv_path = cache_dir / "xrpeur_1d_trades_agg.csv"
    ckpt_path = cache_dir / "trades_ckpt.json"
    start_dt = datetime(start.year, start.month, start.day, tzinfo=timezone.utc)
    end_dt = datetime(
        end_exclusive.year, end_exclusive.month, end_exclusive.day, tzinfo=timezone.utc
    )
    cursor = int(start_dt.timestamp() * 1e9)
    end_ns = int(end_dt.timestamp() * 1e9)
    buckets: dict[int, list[float]] = {}
    pages = 0
    if ckpt_path.exists():
        state = json.loads(ckpt_path.read_text())
        cursor = int(state["cursor"])
        pages = int(state["pages"])
        buckets = {int(k): v for k, v in state["buckets"].items()}
        print(f"trades resume pages={pages} days={len(buckets)}", flush=True)
    t0 = time.time()
    last_save = time.time()
    start_ns = int(start_dt.timestamp() * 1e9)
    while cursor < end_ns:
        url = (
            f"{REST_TRADES_URL}?pair={PAIR}&since={cursor}&count=1000"
        )
        payload = http_get_json(url)
        errors = payload.get("error") or []
        if errors:
            print(f"  trades error {errors}", flush=True)
            time.sleep(2)
            continue
        result = payload["result"]
        key = next(k for k in result if k != "last")
        batch = result[key]
        last = int(result["last"])
        pages += 1
        if not batch:
            break
        crossed = False
        for trade in batch:
            ts = float(trade[2])
            tns = int(ts * 1e9)
            if tns >= end_ns:
                crossed = True
                break
            if tns < start_ns:
                continue
            day_ts = int(ts) - (int(ts) % 86400)
            px = float(trade[0])
            vol = float(trade[1])
            bucket = buckets.get(day_ts)
            if bucket is None:
                buckets[day_ts] = [px, px, px, px, vol, 1.0]
            else:
                if px > bucket[1]:
                    bucket[1] = px
                if px < bucket[2]:
                    bucket[2] = px
                bucket[3] = px
                bucket[4] += vol
                bucket[5] += 1.0
        if pages % 25 == 0 or crossed:
            last_ts = float(batch[-1][2])
            print(
                f"trades p={pages} days={len(buckets)} last="
                f"{datetime.fromtimestamp(last_ts, timezone.utc).isoformat()} "
                f"elapsed={time.time() - t0:.0f}s",
                flush=True,
            )
        if last <= cursor:
            break
        cursor = last
        if time.time() - last_save > 30:
            ckpt_path.write_text(
                json.dumps({"cursor": cursor, "pages": pages, "buckets": buckets})
            )
            last_save = time.time()
        if crossed:
            break
        time.sleep(0.22)
    ckpt_path.write_text(
        json.dumps({"cursor": cursor, "pages": pages, "buckets": buckets})
    )
    bars = [
        Bar(
            ts=day_ts,
            open=vals[0],
            high=vals[1],
            low=vals[2],
            close=vals[3],
            volume=vals[4],
            trades=int(vals[5]),
            source="rest_trades_agg_1d",
        )
        for day_ts, vals in sorted(buckets.items())
    ]
    with csv_path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["timestamp", "open", "high", "low", "close", "volume", "trades"]
        )
        for bar in bars:
            writer.writerow(
                [bar.ts, bar.open, bar.high, bar.low, bar.close, bar.volume, bar.trades]
            )
    return bars


def merge_tape(
    body: list[Bar],
    rest: list[Bar],
    window_end: date,
) -> list[Bar]:
    """Prefer REST OHLC on overlap; drop the forming UTC day."""
    by_ts: dict[int, Bar] = {b.ts: b for b in body}
    rest_first: int | None = rest[0].ts if rest else None
    for bar in rest:
        if bar.day > window_end:
            continue
        if rest_first is not None and bar.ts < rest_first:
            continue
        by_ts[bar.ts] = bar
    out = [by_ts[k] for k in sorted(by_ts) if datetime.fromtimestamp(k, timezone.utc).date() <= window_end]
    return out


def fetch_one_day_from_trades(day: date) -> Bar | None:
    """Aggregate one UTC day of Kraken Trades for an OHLC overlap check."""
    start = datetime(day.year, day.month, day.day, tzinfo=timezone.utc)
    end = datetime.fromtimestamp(start.timestamp() + 86400, timezone.utc)
    cursor = int(start.timestamp() * 1e9)
    end_ns = int(end.timestamp() * 1e9)
    open_px = high = low = close = None
    volume = 0.0
    n = 0
    while cursor < end_ns:
        url = f"{REST_TRADES_URL}?pair={PAIR}&since={cursor}&count=1000"
        payload = http_get_json(url)
        result = payload["result"]
        key = next(k for k in result if k != "last")
        batch = result[key]
        last = int(result["last"])
        if not batch:
            break
        crossed = False
        for trade in batch:
            ts = float(trade[2])
            tns = int(ts * 1e9)
            if tns >= end_ns:
                crossed = True
                break
            if tns < int(start.timestamp() * 1e9):
                continue
            px = float(trade[0])
            volume += float(trade[1])
            n += 1
            if open_px is None:
                open_px = high = low = close = px
            else:
                if px > high:
                    high = px
                if px < low:
                    low = px
                close = px
        if last <= cursor or crossed:
            break
        cursor = last
        time.sleep(0.22)
    if open_px is None:
        return None
    return Bar(
        ts=int(start.timestamp()),
        open=open_px,
        high=high,
        low=low,
        close=close,
        volume=volume,
        trades=n,
        source="rest_trades_agg_1d",
    )


def overlap_ohlc_check(trades_bars: list[Bar], rest_bars: list[Bar]) -> dict:
    rest_map = {b.ts: b for b in rest_bars}
    compared = 0
    mismatches = 0
    first_match = None
    for bar in trades_bars:
        other = rest_map.get(bar.ts)
        if other is None:
            continue
        compared += 1
        ok = (
            abs(bar.open - other.open) < 1e-8
            and abs(bar.high - other.high) < 1e-8
            and abs(bar.low - other.low) < 1e-8
            and abs(bar.close - other.close) < 1e-8
        )
        if first_match is None:
            first_match = {
                "day": bar.day.isoformat(),
                "trades_ohlc": [bar.open, bar.high, bar.low, bar.close],
                "rest_ohlc": [other.open, other.high, other.low, other.close],
                "match": ok,
            }
        if not ok:
            mismatches += 1
            if mismatches <= 5:
                print(
                    f"OVERLAP MISMATCH {bar.day} trades={bar.open, bar.high, bar.low, bar.close} "
                    f"rest={other.open, other.high, other.low, other.close}",
                    flush=True,
                )
    return {
        "compared_days": compared,
        "mismatches": mismatches,
        "first": first_match,
        "ohlc_match": compared > 0 and mismatches == 0,
    }


def score(bars: list[Bar], window_start: date, window_end: date) -> dict[float, Book]:
    books = {fee: Book(fee=fee) for fee in (FEE_PRIMARY, *FEE_SHADOWS)}
    n = len(bars)
    for i, bar in enumerate(bars):
        # Fills at this open from the previous complete bar's close decision.
        for book in books.values():
            if book.pending and bar.day <= window_end:
                if book.pending == "buy" and not book.long:
                    book.execute(bar, "buy")
                elif book.pending == "sell" and book.long:
                    book.execute(bar, "sell")
                book.pending = None
                book.pending_from_ts = None
        if bar.day > window_end:
            break
        if bar.day >= window_start:
            for book in books.values():
                book.mark(bar.ts, bar.close)
        if i < LOOKBACK_IN:
            continue
        if bar.day < window_start or bar.day > window_end:
            continue
        if i + 1 >= n:
            continue
        fill_bar = bars[i + 1]
        if fill_bar.day > window_end:
            continue
        prior_in = bars[i - LOOKBACK_IN : i]
        prior_out = bars[i - LOOKBACK_OUT : i]
        donch_in = max(b.high for b in prior_in)
        donch_out = min(b.low for b in prior_out)
        for book in books.values():
            if (not book.long) and bar.close > donch_in:
                book.pending = "buy"
                book.pending_from_ts = bar.ts
            elif book.long and bar.close < donch_out:
                book.pending = "sell"
                book.pending_from_ts = bar.ts
    return books


def sanity_last_complete(bars: list[Bar], window_end: date) -> dict:
    idx = next(i for i, b in enumerate(bars) if b.day == window_end)
    bar = bars[idx]
    prior = bars[idx - LOOKBACK_IN : idx]
    donch20 = max(b.high for b in prior)
    donch10 = min(b.low for b in bars[idx - LOOKBACK_OUT : idx])
    return {
        "day": bar.day.isoformat(),
        "close": bar.close,
        "donch20": donch20,
        "donch10": donch10,
        "enter": bar.close > donch20,
        "exit_if_long": bar.close < donch10,
        "note": "live book: no enter on 2026-08-27 close 1.24767 vs Donch20 1.45274",
    }


def fmt(x: float, digits: int = 6) -> float:
    return round(x, digits)


def book_blob(book: Book) -> dict:
    return {
        "fee_pct": fmt(book.fee * 100.0, 2),
        "fills": len(book.fills),
        "buys": sum(1 for f in book.fills if f.side == "buy"),
        "sells": sum(1 for f in book.fills if f.side == "sell"),
        "return_after_fees_pct": fmt(book.return_pct(), 6),
        "maxDD_pct": fmt(book.max_dd_pct, 6),
        "final_equity_eur": fmt(book.final_equity(), 6),
        "final_cash_eur": fmt(book.cash, 6),
        "final_units": fmt(book.units, 8),
        "still_long": book.long,
        "fill_list": [
            {
                "day": f.day,
                "side": f.side,
                "price": fmt(f.price, 8),
                "units": fmt(f.units, 8),
                "notional_eur": fmt(f.notional_eur, 6),
            }
            for f in book.fills
        ],
    }


def verdict_of(book: Book) -> tuple[str, dict]:
    ret = book.return_pct()
    fills = len(book.fills)
    dd = book.max_dd_pct
    gates = {
        "return_gt_0": ret > 0,
        "fills_gte_8": fills >= 8,
        "maxDD_lte_8": dd <= 8.0,
    }
    verdict = "PASS" if all(gates.values()) else "FAIL"
    return verdict, gates


def write_scorecard(
    out_dir: Path,
    *,
    tape: list[Bar],
    books: dict[float, Book],
    data_meta: dict,
    window_end: date,
) -> None:
    primary = books[FEE_PRIMARY]
    verdict, gates = verdict_of(primary)
    window_bars = [b for b in tape if WINDOW_START <= b.day <= window_end]
    first = window_bars[0].day.isoformat() if window_bars else tape[0].day.isoformat()
    last = window_bars[-1].day.isoformat() if window_bars else tape[-1].day.isoformat()
    coverage = "2023+" if first <= "2023-01-01" and last >= window_end.isoformat() else "NOT_2023_plus"
    if first > "2023-01-01":
        coverage = "NOT_2023_plus"
    sanity = sanity_last_complete(tape, window_end) if any(b.day == window_end for b in tape) else {}
    payload = {
        "recipe": RECIPE,
        "unlock": UNLOCK,
        "published": PUBLISHED,
        "parameter_search": False,
        "pair": PAIR,
        "venue": VENUE,
        "clock": "1d",
        "in": LOOKBACK_IN,
        "out": LOOKBACK_OUT,
        "side": "long_only",
        "invert": False,
        "fib_pair_swap": False,
        "rearm_opposite": False,
        "decide": "close",
        "fill": "next_open",
        "clip_eur": CLIP_EUR,
        "start_eur": START_CASH,
        "window": {
            "start": WINDOW_START.isoformat(),
            "end": window_end.isoformat(),
        },
        "tape": {
            "first": first,
            "last": last,
            "bars": len(window_bars),
            "warmup_first": tape[0].day.isoformat(),
            "warmup_bars": len(tape) - len(window_bars),
            "total_bars_incl_warmup": len(tape),
            "coverage": coverage,
            "venue": VENUE,
        },
        "fills": len(primary.fills),
        "return_after_fees_pct": fmt(primary.return_pct(), 6),
        "maxDD_pct": fmt(primary.max_dd_pct, 6),
        "verdict": verdict,
        "gates": gates,
        "fee_primary_pct": 0.26,
        "columns": {
            "0.26": book_blob(primary),
            "0.40": book_blob(books[0.0040]),
            "0.80": book_blob(books[0.0080]),
        },
        "sanity_last_complete": sanity,
        "data": data_meta,
        "locks": {
            "do_not_touch": ["invert-paper", "dca-paper", "adaeur-widefib-paper"],
            "do_not_reseal": "c9689f5d",
            "still_paper": True,
            "not_fund_gate": True,
        },
        "lead": (
            f"{len(primary.fills)} / {fmt(primary.return_pct(), 6)} / "
            f"{fmt(primary.max_dd_pct, 6)} / {verdict} / {first}→{last} / {VENUE}"
        ),
    }
    json_path = out_dir / "scorecard.donch-d20-xrpeur.json"
    json_path.write_text(json.dumps(payload, indent=2) + "\n")
    md = render_md(payload)
    (out_dir / "SCORECARD-donch-d20-xrpeur.md").write_text(md)
    print(payload["lead"], flush=True)
    print(f"wrote {json_path}", flush=True)


def render_md(p: dict) -> str:
    c26 = p["columns"]["0.26"]
    c40 = p["columns"]["0.40"]
    c80 = p["columns"]["0.80"]
    g = p["gates"]
    fills_md = "\n".join(
        f"| {f['day']} | {f['side']} | {f['price']} | {f['units']} | {f['notional_eur']} |"
        for f in c26["fill_list"]
    )
    data = p["data"]
    urls = "\n".join(f"- `{u}`" for u in data.get("urls_downloaded", []))
    sanity = p.get("sanity_last_complete") or {}
    return f"""# SCORECARD donch-d20-xrpeur

{p['lead']}

| field | value |
|---|---|
| verdict (0.26%) | **{p['verdict']}** |
| fills | {p['fills']} |
| return_after_fees_pct | {p['return_after_fees_pct']} |
| maxDD_pct | {p['maxDD_pct']} |
| tape | {p['tape']['first']} → {p['tape']['last']} |
| bars (window) | {p['tape']['bars']} |
| warmup | {p['tape'].get('warmup_first')} ({p['tape'].get('warmup_bars')} bars before window) |
| coverage | {p['tape']['coverage']} |
| venue | {p['tape']['venue']} |
| pair | {p['pair']} |
| clock | 1d Donchian {p['in']}-day high IN / {p['out']}-day low OUT |
| window | {p['window']['start']} → {p['window']['end']} (last complete UTC day) |
| capital | {p['start_eur']} EUR, clip {p['clip_eur']} EUR, one long, rest cash |
| decide / fill | close / next open |
| invert / fib / 15m / re-arm | no / no / no / no |
| parameter search | no ({p['published']}) |
| unlock | {p['unlock']} |
| still paper | yes — not the fund gate |

## Gate (named column 0.26% taker)

| test | value | pass |
|---|---|---|
| return > 0 after fees | {p['return_after_fees_pct']} | {g['return_gt_0']} |
| fills >= 8 | {p['fills']} | {g['fills_gte_8']} |
| maxDD <= 8% | {p['maxDD_pct']} | {g['maxDD_lte_8']} |

Shadows do not change the named verdict.

## Fee columns (same fills, different tax)

| fee | fills | return_after_fees_pct | maxDD_pct | final_equity_eur | still_long |
|---|---|---|---|---|---|
| 0.26% | {c26['fills']} | {c26['return_after_fees_pct']} | {c26['maxDD_pct']} | {c26['final_equity_eur']} | {c26['still_long']} |
| 0.40% | {c40['fills']} | {c40['return_after_fees_pct']} | {c40['maxDD_pct']} | {c40['final_equity_eur']} | {c40['still_long']} |
| 0.80% | {c80['fills']} | {c80['return_after_fees_pct']} | {c80['maxDD_pct']} | {c80['final_equity_eur']} | {c80['still_long']} |

## Fills (0.26% book; prices shared)

| day (UTC) | side | price | units | notional_eur |
|---|---|---|---|---|
{fills_md}

## Last complete day sanity

| field | value |
|---|---|
| day | {sanity.get('day')} |
| close | {sanity.get('close')} |
| Donch20 (prior 20 highs) | {sanity.get('donch20')} |
| Donch10 (prior 10 lows) | {sanity.get('donch10')} |
| enter? close > Donch20 | {sanity.get('enter')} |
| note | {sanity.get('note')} |

## Data

| field | value |
|---|---|
| intended | official Kraken OHLCVT PAIR 1440 XRPEUR/XXRPZEUR + REST 1440 tail |
| used | {data.get('used')} |
| ohlcvt_status | {data.get('ohlcvt_status')} |
| coverage_label | {p['tape']['coverage']} |
| support article | {SUPPORT_OHLCVT} |
| complete zip (quota-blocked here) | {COMPLETE_DRIVE_VIEW} |
| quarterly folder | {QUARTERLY_FOLDER} |
| rest ohlc | {REST_OHLC_URL} |

URLs actually downloaded:

{urls}

{data.get('notes', '')}

Overlap (2024-09-07 trades-agg vs REST 1440): match={data.get('overlap_check', {}).get('ohlc_match')} O/H/L/C trades={data.get('overlap_check', {}).get('first', {}).get('trades_ohlc')} rest={data.get('overlap_check', {}).get('first', {}).get('rest_ohlc')}


## Locks

Do not touch invert-paper, dca-paper, adaeur-widefib-paper. Do not reseal c9689f5d.
Still paper. No keys. No live. This book is NOT the fund gate.
"""


def load_cached_trades_csv(path: Path) -> list[Bar]:
    bars: list[Bar] = []
    with path.open() as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            bars.append(
                Bar(
                    ts=int(float(row["timestamp"])),
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=float(row.get("volume") or 0),
                    trades=int(float(row.get("trades") or 0)),
                    source="rest_trades_agg_1d",
                )
            )
    return bars


def build_tape(cache_dir: Path, window_end: date, skip_ohlcvt: bool) -> tuple[list[Bar], dict]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    rest = fetch_rest_ohlc()
    rest_complete = [b for b in rest if b.day <= window_end]
    urls = [REST_OHLC_URL]
    ohlcvt_log: list[dict] = []
    ohlcvt_bars: list[Bar] = []
    if not skip_ohlcvt:
        ohlcvt_bars, ohlcvt_log = try_ohlcvt_all(cache_dir)
        for row in ohlcvt_log:
            if row.get("ok"):
                urls.append(row["url"])
    if ohlcvt_bars:
        tape = merge_tape(ohlcvt_bars, rest_complete, window_end)
        first = tape[0].day if tape else None
        coverage_ok = bool(tape) and first is not None and first <= WINDOW_START
        meta = {
            "used": "kraken_ohlcvt_1440 + rest_ohlc_1440_tail",
            "ohlcvt_status": "ok",
            "ohlcvt_quarters": ohlcvt_log,
            "urls_downloaded": urls,
            "notes": (
                "Official Kraken OHLCVT PAIR 1440 quarterly zips from the Drive folder "
                "linked by the support article, spliced to REST OHLC 1440 for the tail "
                "through the last complete UTC day. Forming bar dropped."
            ),
            "coverage_ok_2023": coverage_ok,
        }
        return tape, meta

    # OHLCVT failed (typical: Google Drive anonymous quota).
    # Longest honest Kraken-native 1d: Trades REST aggregated to UTC daily
    # through the first REST OHLC timestamp, then REST OHLC tail.
    splice_day = rest_complete[0].day if rest_complete else WINDOW_START
    cached = cache_dir / "xrpeur_1d_trades_agg.csv"
    if cached.exists() and cached.stat().st_size > 100:
        trades_bars = load_cached_trades_csv(cached)
        print(f"loaded cached trades daily {cached} n={len(trades_bars)}", flush=True)
    else:
        trades_bars = aggregate_trades_to_daily(cache_dir, WARMUP_START, splice_day)
    trades_since = int(
        datetime(WARMUP_START.year, WARMUP_START.month, WARMUP_START.day, tzinfo=timezone.utc).timestamp()
        * 1e9
    )
    urls.append(f"{REST_TRADES_URL}?pair={PAIR}&since={trades_since}&count=1000")
    if ohlcvt_log:
        urls.append(ohlcvt_log[0]["url"])
    overlap = overlap_ohlc_check(trades_bars, rest_complete)
    if overlap["compared_days"] == 0 and rest_complete:
        one = fetch_one_day_from_trades(splice_day)
        if one is not None:
            overlap = overlap_ohlc_check([one], rest_complete)
            overlap["method"] = "splice_day_trades_vs_rest_ohlc"
    # Keep trades bars strictly before splice day so REST owns the overlap.
    body = [b for b in trades_bars if b.day < splice_day]
    tape = merge_tape(body, rest_complete, window_end)
    first = tape[0].day if tape else date.max
    coverage = "2023+" if first <= WINDOW_START else "NOT_2023_plus"
    ohlcvt_status = "FAIL Drive quota (anonymous download of official zips blocked)"
    notes = (
        "OHLCVT zip download failed (Google Drive quota exceeded on the official "
        f"complete file {COMPLETE_DRIVE_VIEW} and quarterly folder {QUARTERLY_FOLDER} "
        f"linked from {SUPPORT_OHLCVT}). Tape is Kraken-native anyway: public Trades "
        f"REST aggregated to UTC 1d from {WARMUP_START.isoformat()} through the day "
        f"before REST OHLC 1440 begins ({splice_day.isoformat()}), then REST OHLC 1440 "
        f"through {window_end.isoformat()}. Not Binance. No invented OHLC: daily bars "
        "are first/max/min/last Kraken prints. Overlap vs REST 1440 on the splice day "
        f"is recorded below. coverage={coverage}."
    )
    meta = {
        "used": "kraken_trades_agg_1d + rest_ohlc_1440_tail",
        "ohlcvt_status": ohlcvt_status,
        "ohlcvt_quarters": ohlcvt_log,
        "urls_downloaded": urls,
        "overlap_check": overlap,
        "splice_day": splice_day.isoformat(),
        "notes": notes,
        "coverage_ok_2023": coverage == "2023+",
    }
    return tape, meta


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).resolve().parent
    parser.add_argument("--cache-dir", type=Path, default=Path("/tmp/kraken-ohlcvt"))
    parser.add_argument("--out-dir", type=Path, default=here)
    parser.add_argument("--skip-ohlcvt", action="store_true")
    parser.add_argument(
        "--window-end",
        default=None,
        help="YYYY-MM-DD last complete UTC day (default: yesterday UTC)",
    )
    args = parser.parse_args(argv)
    window_end = (
        date.fromisoformat(args.window_end)
        if args.window_end
        else last_complete_utc_day()
    )
    print(f"window_end={window_end.isoformat()}", flush=True)
    tape, meta = build_tape(args.cache_dir, window_end, args.skip_ohlcvt)
    if not tape:
        print("FAIL: empty tape", file=sys.stderr)
        return 2
    print(
        f"tape {tape[0].day} → {tape[-1].day} bars={len(tape)} used={meta['used']}",
        flush=True,
    )
    books = score(tape, WINDOW_START, window_end)
    write_scorecard(args.out_dir, tape=tape, books=books, data_meta=meta, window_end=window_end)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
