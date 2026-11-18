#!/usr/bin/env python3
"""Pre-flight lint for Example Electric blog deliverables.

Usage:
  lint_post.py <slug>-post.html [<slug>-schema.txt] [--min-words 1800] [--max-words 2600]

Exit 0 = clean. Exit 1 = one or more FAIL lines. WARN lines never block.
Every check here corresponds to a defect that reached a live page or a delivery at least once, so removing a
check re-opens a known hole; add checks as new defects appear. Runs the content-humanizer scorer as a warning
when that plugin is installed.
"""
import sys, re, json, html, argparse, pathlib

BANNED = [
    (r"\bmaster[\s-]*electrician\b", "'Master Electrician' is a misrepresented credential"),
    (r"\bauthori[sz]ed\s+dealer\b", "'Authorized Dealer' claim not held (use 'Generac-trained')"),
    (r"powerpro\s+premier", "'PowerPro Premier' not held"),
    (r"555[\s.-]?0199", "old phone number 503-555-0199"),
    (r"\bfree\b(?!-)", "the word 'free' (reword: 'at no cost' for third-party facts only)"),
    (r"<h1\b", "<h1> inside post HTML (Divi renders the title)"),
    (r"ion-icon|unpkg\.com|cdn\.jsdelivr|cdnjs", "CDN icon/script dependency (use inline SVG)"),
    (r"ea-sticky-call", "per-post sticky call bar (sitewide snippet handles it)"),
    (r"blockquote[^>]*ea-owner|owner'?s\s+take|owner&rsquo;s\s+take", "founder blockquote / Owner's Take"),
    (r"\bIMAGE_URL\b|IMAGE_URL_HERE|src=\"\"|src='#'|src=\"#\"|placeholder\.(jpg|png|webp)", "placeholder image src"),
    (r"&#8212;|&#x2014;", "em dash as numeric entity"),
    (r"\bBDS\b|Bureau of Development Services", "BDS is gone; use Portland Permitting & Development (PP&D)"),
    (r"ccb\.oregon\.gov", "dead CCB URL; use https://www.oregon.gov/ccb/pages/default.aspx"),
]
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]")

def strip_tags(s):
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", s))

def meta_field(src, name):
    m = re.search(r"^\s*" + re.escape(name) + r":\s*(.+?)\s*$", src, flags=re.M)
    return m.group(1).strip() if m else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("post"); ap.add_argument("schema", nargs="?")
    ap.add_argument("--min-words", type=int, default=1800); ap.add_argument("--max-words", type=int, default=2600)
    a = ap.parse_args()
    fails, warns = [], []
    src = pathlib.Path(a.post).read_text(encoding="utf-8")

    # --- encoding
    bad = sorted({c for c in src if ord(c) > 127})
    if bad: fails.append(f"non-ASCII characters present: {bad!r} (use HTML entities / CSS escapes)")
    if "\u2014" in src or "&mdash;" in strip_tags(src): fails.append("em dash in body copy")
    if EMOJI.search(src): fails.append("emoji present")

    # --- banned phrases (everything except the <style> block; CSS is allowed to name selectors)
    scan = re.sub(r"<style[^>]*>.*?</style>", " ", src, flags=re.S)
    def ban_scan(text, label):
        for pat, why in BANNED:
            m = re.search(pat, text, flags=re.I)
            if m:
                ctx = text[max(0, m.start()-40): m.end()+40].replace("\n", " ")
                fails.append(f"{label}{why}: ...{ctx}...")
    ban_scan(scan, "")                       # raw HTML (catches placeholders, CDN tags)
    ban_scan(strip_tags(scan), "[rendered text] ")  # catches 'Master <strong>Electrician'
    for m in re.finditer(r'<img[^>]+src="([^"]*)"', scan):
        if not m.group(1).startswith("https://client.example/"):
            fails.append(f"img src is not on client.example (placeholder or hotlink): {m.group(1)[:60]}")

    # --- structure
    body = src.split('<div class="ea-post">', 1)
    if len(body) < 2: fails.append('missing <div class="ea-post"> wrapper')
    else:
        b = body[1]
        if 'class="ea-updated"' not in b: fails.append("missing 'Last updated' line (.ea-updated)")
        if 'class="ea-hero-stats"' not in b: warns.append("no hero stat row")
        if 'class="ea-trust-bar"' not in b: fails.append("missing trust bar")
        if "EXAMPLE000XX" not in b: fails.append("Washington license EXAMPLE000XX missing from post")
        if "000000" not in b: fails.append("Oregon CCB# 000000 missing from post")
        if 'class="ea-faq"' not in b: fails.append("missing FAQ block")
        if b.count("<details") < 5: fails.append(f"FAQ has {b.count('<details')} questions; need 5-7")
        if b.count("<details open") < 2: warns.append("fewer than two FAQ items open by default")
        if 'class="ea-final-cta"' not in b: fails.append("missing final CTA block")
        if 'class="ea-cta-inline"' not in b: warns.append("no inline CTA")
        if 'class="ea-sources"' not in b: fails.append("missing Sources block")
        ext = re.findall(r'href="(https?://[^"]+)"', b)
        primary = [u for u in ext if re.search(r"oregon\.gov|portland\.gov|public\.law|lni\.wa\.gov|portlandgeneral|clarkpublicutilities|nwnatural|energytrust|irs\.gov|nfpa\.org|clark\.wa\.gov|multco|clackamas|washingtoncounty", u)]
        if len(primary) < 2: fails.append(f"only {len(primary)} primary-source links; need 2-5")
        internal = re.findall(r'href="(/[^"]+)"', b)
        if len(internal) < 3: fails.append(f"only {len(internal)} internal links; need 3+")
        text = strip_tags(b)
        words = len(text.split())
        if words < 1200: fails.append(f"{words} words; under 1,200 is not a guide")
        elif words < a.min_words: warns.append(f"{words} words; target band starts at {a.min_words} (length is a byproduct, do not pad)")
        elif words > a.max_words: warns.append(f"{words} words; above {a.max_words}")
        first_p = re.search(r'<p(?![^>]*class="ea-updated")[^>]*>(.*?)</p>', b, flags=re.S)
        intro = html.unescape(re.sub(r"<[^>]+>", " ", first_p.group(1))).strip() if first_p else ""
        # the rule is "never open with a rhetorical question"; a subordinate clause starting
        # with When/While is fine, so test the first sentence for an actual question mark
        first_sentence = re.split(r"(?<=[.!?])\s", intro.strip())[0] if intro.strip() else ""
        if first_sentence.rstrip().endswith("?"):
            fails.append(f"intro opens with a question: {first_sentence[:70]}")
        for m in re.finditer(r'<img[^>]+>', b):
            if 'alt="' not in m.group(0): fails.append("img without alt text")
            else:
                alt = re.search(r'alt="([^"]*)"', m.group(0)).group(1)
                n = len(alt.split())
                if n < 6 or n > 20: warns.append(f"alt text {n} words (aim 8-16): {alt[:60]}")

    # --- meta comment
    seo = meta_field(src, "SEO Title"); meta = meta_field(src, "Meta description"); exc = meta_field(src, "Excerpt")
    wp = meta_field(src, "Title"); slug = meta_field(src, "Slug"); gain = meta_field(src, "Information gain")
    if not wp: fails.append("meta comment missing 'Title' (WP post title)")
    if not slug: fails.append("meta comment missing 'Slug'")
    if not seo: fails.append("meta comment missing 'SEO Title'")
    elif len(seo) > 60: fails.append(f"SEO Title {len(seo)} chars (max 60)")
    if not meta: fails.append("meta comment missing 'Meta description'")
    else:
        if len(meta) > 160: fails.append(f"Meta description {len(meta)} chars (max 160)")
        if not meta.rstrip().endswith("Call (503) 555-0100."): fails.append("Meta description must end with 'Call (503) 555-0100.'")
    if not exc: fails.append("meta comment missing 'Excerpt'")
    else:
        n = len(exc.split())
        if n < 50 or n > 70: warns.append(f"Excerpt {n} words (aim 50-70)")
    if not gain: warns.append("meta comment missing 'Information gain'")

    # --- schema
    if a.schema:
        s = pathlib.Path(a.schema).read_text(encoding="utf-8")
        st = s.strip()
        if not st.startswith("<script"): fails.append("schema file must START with <script")
        if not st.endswith("</script>"): fails.append("schema file must END with </script>")
        if any(ord(c) > 127 for c in s): fails.append("schema contains non-ASCII")
        if "\u2014" in s: fails.append("schema contains em dash")
        try:
            d = json.loads(st.split(">", 1)[1].rsplit("</script>", 1)[0])
            faqs = d.get("mainEntity", {}).get("mainEntity", [])
            vis = re.findall(r"<summary>(.*?)</summary>", src, flags=re.S)
            vis = [html.unescape(re.sub(r"<[^>]+>", "", v)).strip() for v in vis]
            for q in faqs:
                if q.get("name", "").strip() not in vis:
                    fails.append(f"schema FAQ not visible on page verbatim: {q.get('name','')[:70]}")
            upd = re.search(r'class="ea-updated">Last updated ([^<]+)<', src)
            if upd and d.get("dateModified"):
                import datetime
                try:
                    dt = datetime.datetime.strptime(upd.group(1).strip(), "%B %d, %Y").date().isoformat()
                    if dt != d["dateModified"]: fails.append(f"Last updated ({dt}) != schema dateModified ({d['dateModified']})")
                except ValueError: warns.append("could not parse Last updated date")
            imgs = d.get("image")
            if imgs and any(not str(u).startswith("https://client.example/") for u in imgs):
                fails.append("schema image URL is not on client.example (placeholder?)")
            if slug and slug not in d.get("mainEntityOfPage", {}).get("@id", ""): fails.append("schema mainEntityOfPage @id does not contain the slug")
            ban_scan(s, "[schema] ")
            # template placeholders like [WP title] or [YYYY-MM-DD]; a JSON array of quoted
            # strings (e.g. hasCredential) is legitimate, so brackets containing a quote are skipped
            ph = [m for m in re.findall(r"\[[^\]\n]{1,60}\]", s) if '"' not in m]
            if ph: fails.append(f"schema has unreplaced template placeholders: {ph[:3]}")
        except Exception as e:
            fails.append(f"schema JSON invalid: {e}")

    # --- content-humanizer score (warning only). Plugin: marketing-skills content-humanizer.
    scorer = next(iter(sorted(pathlib.Path.home().glob(".claude/plugins/cache/*/marketing-skills/*/content-humanizer/scripts/humanizer_scorer.py"))), None)
    if scorer and len(body) > 1:
        import subprocess, tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as tf:
            tf.write(strip_tags(body[1])); tmp = tf.name
        try:
            out = subprocess.run([sys.executable, str(scorer), tmp, "--json"], capture_output=True, text=True, timeout=60).stdout
            js = json.loads(out[out.index("{"):]) if "{" in out else {}
            score = js.get("score") or js.get("humanity_score") or js.get("total")
            if score is not None:
                print(f"INFO  content-humanizer score {score}/100" + ("" if float(score) >= 80 else "  (run /content-humanizer Mode 2 before delivery)"))
                if float(score) < 80: warns.append(f"humanizer score {score}/100 below 80")
        except Exception as e:
            print(f"INFO  humanizer scorer skipped: {e}")
    for w in warns: print(f"WARN  {w}")
    for f in fails: print(f"FAIL  {f}")
    print(f"\n{'CLEAN' if not fails else 'BLOCKED'}: {len(fails)} fail, {len(warns)} warn")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
