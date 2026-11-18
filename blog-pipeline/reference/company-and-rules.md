# Company context and non-negotiable rules

Every rule here is enforced by `scripts/lint_post.py` where a machine can check it. The rest is judgment, and the auditor agent checks it.

## Company

| Field | Value |
|---|---|
| Business | Example Electric (a placeholder: the real client's name, owner, address, phone and license numbers are replaced throughout this copy) |
| Owner | [Owner name], Licensed Electrician. Never "Master Electrician". |
| Licenses | Oregon CCB# 000000. Washington Electrical Contractor EXAMPLE000XX (all caps). Both, always. |
| Phone | (503) 555-0100. The old 503-555-0199 must never appear anywhere, including image files and logo artwork. `Example_Electric-Gold_Logo_WA-white.png` has the old number baked in; never use it. |
| Address | [business address]. Match the Google Business Profile exactly; do not add a suite number until it is confirmed there. |
| Oregon area | Portland metro: Multnomah, Clackamas, Washington counties. Portland, Beaverton, Lake Oswego, Hillsboro, Tigard, West Linn, Milwaukie, Oregon City, Canby, Gresham. |
| Washington area | Vancouver, Camas, Washougal, Battle Ground, Ridgefield, La Center, Clark County |
| Differentiators | [ownership differentiators]. 24/7 emergency. Permits filed for you. Licensed on both sides of the river. Same-week scheduling for most projects. |
| Reviews | [review counts]. One rounded sitewide figure in copy; re-check the live Google Business Profile before changing it; schema uses the true count. |
| Website | https://client.example. Blog posts live at `/blog/<slug>/`. |
| Tone | Expert, plain-spoken, direct. The owner's voice: experienced and honest, not salesy, occasionally dry. |

## Hard bans (lint enforced)

| Never | Use instead |
|---|---|
| "free" in any customer-facing sense: free assessment, free quote, free estimate, free load calc, free consultation, "Get a free ..." | "on-site assessment", "site visit", "load calculation", "quote", "estimate", "Same-week scheduling for most projects" |
| "Master Electrician" in any casing or hyphenation | "Licensed Electrician", "Oregon-licensed electrician", "Licensed under Oregon CCB# 000000" |
| "Generac Authorized Dealer", "PowerPro Premier", any "Authorized [Brand] Dealer" | "Generac-trained", "Generac factory-trained for Air-Cooled Home Standby Installation" |
| 503-555-0199 in any format | (503) 555-0100 |
| Em dashes in body copy | Commas, colons, periods, "and" |
| Emojis | Inline SVG icons from `reference/template.md` |
| Literal non-ASCII characters | HTML entities in body (`&ndash;` `&middot;` `&deg;` `&rsquo;` `&ldquo;` `&rdquo;` `&hellip;`); CSS escapes in `content:` (`"\2212"` `"\201C"`) |
| `<h1>` inside the post HTML | Divi renders the title from the WP title field |
| `ion-icon`, unpkg, any CDN script | Inline SVG |
| `.ea-sticky-call` element or CSS | The sitewide WPCode snippet handles the sticky bar |
| `blockquote.ea-owner`, "Owner's Take", first-person owner quotes | Flow the body into the FAQ. Bylines are fine, in-body founder quotes are not. |
| Placeholder image `src` (IMAGE_URL_HERE etc.) | Omit the figure until the real URL exists |
| Plain text above `<script` in the schema file | Nothing. The schema file is pure script. |

**Third-party programs: reword, keep the fact.** "PGE provides a backup power transfer meter at no cost" is correct. Deleting the fact to dodge the word is not. Never bulk find-and-replace the bare word "free" (that produced "Get a Book a" on the live site); rewrite the sentence.

## Judgment rules (auditor enforced)

- **Answer first.** The key takeaway is in the first two sentences. Never open with a question. No "In today's world".
- **Self-contained sentences.** "In Oregon, replacing a panel does not require AFCI on existing circuits" reads correctly when lifted out of context by an AI engine. "This is not required here" does not.
- **Question-format H2s** where natural, each answered directly in its first sentence.
- **Honest limits.** Say when something is not required, when the cheaper option is fine, when a reader does not need an electrician. Anti-upsell content is the strongest trust signal available and it converts.
- **First-hand markers.** "What we see on Portland service calls", "on a 1920s Sellwood service". Only where true; never invent a job.
- **No unverifiable job claims** in captions or alt text. Describe what is visible.
- **No location tags on residential job photos.** Metro level only.
- **Jurisdiction discipline.** Decide Oregon, Washington, or both before writing. Permits, licensing, homeowner exemptions and code amendments differ. `areaServed` in schema must match.
- **Estimates are labelled.** A dollar range that is not from a published source is a planning number and the post says so. The delivery message lists which figures are verified and which are estimates.
- **Length is a byproduct.** Target 1,800-2,500 words by covering the topic, never by padding.

## Encoding rule

HTML body uses entities: `&ndash;` `&mdash;`(avoid) `&deg;` `&middot;` `&times;` `&lsquo;` `&rsquo;` `&ldquo;` `&rdquo;` `&hellip;` `&#9733;`.

CSS `content:` does not parse entities. Use escapes: `"\00A7"` `"\2212"` `"\201C"` `"\201D"` `"\2014"`. If literal entity text renders before a heading, a find-and-replace converted CSS escapes to entities; restore the `\hex` form.

## Divi rules

- Colours: `.ea-post > p { color: var(--ea-text) !important; }` scoped to direct children only. A bare `.ea-post p { !important }` overrides the white text inside navy CTA blocks and renders dark-on-dark.
- Section and row: fullwidth, gutter width 1, zero padding, page title hidden. Otherwise the module clips with a stray "Home" heading.
- Schema goes in WPCode, never in the Code module. Divi corrupts JSON on save.
- WordPress auto-places the featured image; the post HTML does not include it.
