#!/usr/bin/env python3
"""Rank blog topic candidates from a Google Search Console export folder.

Usage:
  gsc_gaps.py <export_dir> [--existing-slugs slugs.txt] [--top 15]

<export_dir> is the folder GSC produces (Queries.csv, Pages.csv, Chart.csv, Filters.csv ...).
Prints: the data window, clusters of non-brand queries ranked by opportunity, whether an existing
post already targets the cluster (cannibalization check), and the informational queries with the
most impressions and zero clicks. This is the fallback when the Ahrefs MCP returns "Insufficient plan".
"""
import csv, re, sys, argparse, pathlib
from collections import defaultdict

BRAND = ("example electric", "exampleelectric", "electric example", "example elec ")
CLUSTERS = {
    "service upgrade / amperage": r"\b(100|125|150|200)\s?amp|service upgrade|upgrade.*service|meter (base|socket)|main breaker",
    "panel upgrade / replacement": r"panel (upgrade|replace|swap)|breaker (panel|box)|electrical panel",
    "old panels (FPE/Zinsco/Pushmatic)": r"federal pacific|fpe|zinsco|pushmatic|split.?bus|stab.?lok|fuse box",
    "hot tub / spa": r"hot tub|\bspa\b",
    "sauna": r"sauna",
    "cold plunge": r"cold plunge",
    "ev charger": r"\bev\b|electric vehicle|charger|level 2|tesla",
    "generator / standby": r"generator|generac|standby|backup power",
    "battery / solar": r"battery|powerwall|solar",
    "rewiring / knob and tube / aluminum": r"rewir|knob|aluminum|cloth wir|old wiring",
    "outlet / switch symptoms": r"outlet|receptacle|gfci|smok|spark|burn|buzz|hum|flicker|trip",
    "emergency": r"emergency|24.?7|24 hour",
    "permits / DIY / homeowner": r"permit|homeowner|myself|my own|diy|inspection",
    "heat pump / HVAC": r"heat pump|hvac|mini.?split|furnace|air condition",
    "ADU / remodel / new construction": r"\badu\b|remodel|new construction|addition",
    "commercial": r"commercial|tenant|business|office|restaurant|warehouse",
    "lighting": r"light(ing)?\b|recessed|chandelier|landscape",
    "vancouver / clark county WA": r"vancouver|camas|washougal|clark county|battle ground|ridgefield",
}

def num(x): return float(str(x).replace("%", "").replace(",", "") or 0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export_dir"); ap.add_argument("--existing-slugs"); ap.add_argument("--top", type=int, default=15)
    a = ap.parse_args()
    d = pathlib.Path(a.export_dir)
    filt = dict(csv.reader(open(d / "Filters.csv", encoding="utf-8-sig")))
    ch = list(csv.DictReader(open(d / "Chart.csv", encoding="utf-8-sig")))
    print(f"WINDOW: {filt.get('Date','?')} | {ch[0]['Date']} to {ch[-1]['Date']} | {len(ch)} days | "
          f"{sum(num(r['Clicks']) for r in ch):.0f} clicks | {sum(num(r['Impressions']) for r in ch):.0f} impressions")
    print("NOTE: page and query totals below are for this window only. Never compare to a different window.\n")

    q = list(csv.DictReader(open(d / "Queries.csv", encoding="utf-8-sig")))
    qk = "Top queries"
    nb = [r for r in q if not any(b in r[qk].lower() for b in BRAND)]
    pages = list(csv.DictReader(open(d / "Pages.csv", encoding="utf-8-sig")))
    slugs = [re.sub(r"^https?://[^/]+", "", p["Top pages"]).strip("/") for p in pages]
    if a.existing_slugs:
        slugs += [s.strip() for s in open(a.existing_slugs) if s.strip()]

    rows = []
    for name, pat in CLUSTERS.items():
        p = re.compile(pat, re.I)
        m = [r for r in nb if p.search(r[qk])]
        if not m: continue
        imps = sum(num(r["Impressions"]) for r in m); clk = sum(num(r["Clicks"]) for r in m)
        wpos = sum(num(r["Position"]) * num(r["Impressions"]) for r in m) / imps if imps else 0
        covering = sorted({s for s in slugs if p.search(s.replace("-", " "))})
        rows.append((name, len(m), imps, clk, wpos, covering, sorted(m, key=lambda r: -num(r["Impressions"]))[:3]))
    rows.sort(key=lambda r: -r[2])
    print(f"{'CLUSTER':40} {'q':>3} {'imps':>7} {'clk':>4} {'wpos':>5}  COVERED BY")
    for name, n, imps, clk, wpos, cov, top in rows[: a.top]:
        cv = ", ".join(cov[:3]) + (" ..." if len(cov) > 3 else "") if cov else "NONE  <-- gap"
        print(f"{name:40} {n:>3} {imps:>7.0f} {clk:>4.0f} {wpos:>5.1f}  {cv}")
        for r in top:
            print(f"    {r[qk][:58]:58} imps {num(r['Impressions']):>6.0f} pos {num(r['Position']):>5.1f} clk {num(r['Clicks']):.0f}")

    print("\nINFORMATIONAL, ZERO-CLICK, POSITIONS 4-20 (content that would answer these does not exist yet):")
    info = re.compile(r"\b(how|why|what|when|can|do|does|is|should|cost to|much|vs|keeps?|won'?t|not working|need)\b", re.I)
    cand = [r for r in nb if info.search(r[qk]) and num(r["Clicks"]) == 0 and 4 <= num(r["Position"]) <= 20]
    for r in sorted(cand, key=lambda r: -num(r["Impressions"]))[:15]:
        print(f"  {r[qk][:64]:64} imps {num(r['Impressions']):>6.0f} pos {num(r['Position']):>5.1f}")

    print("\nCTR REALITY CHECK (AI-surface inflation):")
    top3 = [r for r in nb if num(r["Position"]) <= 3 and num(r["Impressions"]) >= 50]
    if top3:
        ci = sum(num(r["Impressions"]) for r in top3); cc = sum(num(r["Clicks"]) for r in top3)
        print(f"  non-brand queries at position <=3 with 50+ impressions: {len(top3)} | CTR {100*cc/ci:.2f}% (human baseline 15-28%)")
        print("  If CTR is under 2%, impressions are AI fan-out. Do not chase them with title rewrites.")

if __name__ == "__main__":
    main()
