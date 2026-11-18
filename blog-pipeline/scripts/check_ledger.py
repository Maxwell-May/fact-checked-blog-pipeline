#!/usr/bin/env python3
"""Gate on a checked claim ledger before writing. Fails CLOSED on anything it cannot parse.

Usage: check_ledger.py <checked-ledger.md>

Exit 0 (GATE OPEN) only when: exactly one table with a 'Check result' column; every row has the same
cell count as the header; every row's Check result is CONFIRMED / CONFIRMED-SECONDARY / CORRECTED /
ESTIMATE / DROPPED; every non-DROPPED row names a source in the Source column (a URL, a rendered
Table 1-E page image, or for ESTIMATE rows a named provenance); and at least one usable row exists.
Anything else exits 1 (BLOCKED) and lists the rows. DROPPED rows pass but must not appear in the post.
CONFIRMED-SECONDARY rows (NEC text confirmed via a tier-2 source because NFPA text is paywalled) pass
but are listed so the delivery message can disclose them.
"""
import sys, re, pathlib

OK = {"CONFIRMED", "CONFIRMED-SECONDARY", "CORRECTED", "ESTIMATE", "DROPPED"}
KNOWN = OK | {"UNVERIFIED", "CONFLICT", "SECONDARY", "UNCHECKED"}
SRC_RE = re.compile(r"https?://|render_table1e|\.png\b")

def split_cells(line):
    """Split a markdown table row on pipes that are not inside backticks."""
    out, buf, tick = [], [], False
    for ch in line.strip():
        if ch == "`": tick = not tick
        if ch == "|" and not tick: out.append("".join(buf)); buf = []
        else: buf.append(ch)
    out.append("".join(buf))
    if out and out[0].strip() == "": out = out[1:]
    if out and out[-1].strip() == "": out = out[:-1]
    return [c.strip() for c in out]

def main():
    if len(sys.argv) != 2:
        print("usage: check_ledger.py <checked-ledger.md>"); sys.exit(2)
    t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    lines = [l.strip() for l in t.splitlines() if l.strip().startswith("|")]
    headers = [l for l in lines if "check result" in l.lower()]
    if len(headers) != 1:
        print(f"BLOCKED: expected exactly one table header with a 'Check result' column, found {len(headers)}. "
              "The claim checker must return one merged table with one header."); sys.exit(1)
    header = headers[0]
    hcells = [c.lower() for c in split_cells(header)]
    ci = hcells.index("check result")
    si = next((i for i, c in enumerate(hcells) if c.startswith("source")), None)
    if si is None:
        print("BLOCKED: no 'Source' column in the header."); sys.exit(1)
    counts, bad, est, sec = {}, [], [], []
    rows = 0
    for l in lines:
        if l == header or re.match(r"^\|[-\s|:]+\|$", l): continue
        cells = split_cells(l); rows += 1
        claim = cells[1][:90] if len(cells) > 1 else l[:90]
        if len(cells) != len(hcells):
            counts["MALFORMED"] = counts.get("MALFORMED", 0) + 1
            bad.append((f"MALFORMED ({len(cells)} cells vs {len(hcells)})", claim)); continue
        res = cells[ci].upper().strip() or "UNCHECKED"
        if res not in KNOWN: res = "UNCHECKED"
        counts[res] = counts.get(res, 0) + 1
        src = cells[si]
        has_src = bool(SRC_RE.search(src))
        if res == "ESTIMATE" and src.lower() not in {"", "n/a", "none", "-"}: has_src = True
        if res not in OK: bad.append((res, claim))
        elif res != "DROPPED" and not has_src: bad.append(("NO SOURCE (Source column needs a URL or page image)", claim))
        if res == "ESTIMATE": est.append(cells[1][:110])
        if res == "CONFIRMED-SECONDARY": sec.append(cells[1][:110])
    usable = sum(counts.get(k, 0) for k in ("CONFIRMED", "CONFIRMED-SECONDARY", "CORRECTED", "ESTIMATE"))
    print("LEDGER COUNTS: " + ("  ".join(f"{k}: {v}" for k, v in sorted(counts.items())) or "none"))
    if est:
        print("\nESTIMATES (must be labelled as planning numbers in the post):")
        for e in est: print("  - " + e)
    if sec:
        print("\nCONFIRMED VIA TIER-2 SOURCE (disclose in delivery; NEC text via Mike Holt / EC&M / IAEI):")
        for e in sec: print("  - " + e)
    if rows == 0 or usable == 0:
        print("\nBLOCKED: no usable rows. Nothing to write from."); sys.exit(1)
    if bad:
        print("\nBLOCKING ROWS:")
        for r, c in bad: print(f"  [{r}] {c}")
        print("\nBLOCKED: fix or drop these rows before writing."); sys.exit(1)
    print("\nGATE OPEN: write from CONFIRMED/CORRECTED rows; label ESTIMATE rows; DROPPED rows must not appear in any form.")

if __name__ == "__main__":
    main()
