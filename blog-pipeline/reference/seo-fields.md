# SEO fields, delivery block, and GBP companion

## Delivery block (always all of it, in this order)

The WP title was dropped from a delivery once because it only lived in the meta comment. Every delivery prints this table:

| Field | Rule |
|---|---|
| **WP Post Title (H1)** | Descriptive, natural, may exceed 60 chars. Rendered by Divi from the WP title field. |
| **Slug** | Lowercase, hyphens, no year (posts get refreshed; URLs do not). |
| **Rank Math SEO Title** | **60 chars max.** Focus keyword first, city, year when cost or code driven. No "How much does", no trailing "Cost & Code Guide", plain ASCII. |
| **Focus keyword** | The query the post targets; must appear in title, first paragraph, one H2. |
| **Meta description** | **160 chars max**, plain ASCII, **ends with `Call (503) 555-0100.`** Lead with the price range on cost posts. Honest urgency hook where one exists. Drop the year, then the license number, if tight. |
| **Excerpt** | 50-70 words, reader-facing, no CTA. Powers the archive, Recent Posts, RSS. |
| **Category** | Blog |
| **Tags** | 3-6, the cluster name plus jurisdiction (e.g. `hot tub`, `spa wiring`, `Portland`, `Oregon code`) |
| **Author** | Example Electric (site default) until the owner's author page exists |
| **Publish date** | `datePublished` in the schema = the day it goes live; `dateModified` = the Last updated line. If publishing slips a day, update both before activating the WPCode snippet. |
| **Featured image** | Set in WordPress, not in the HTML. 1200x675 minimum (16:9), descriptive filename, alt text 8-16 words, no residential location tags. |
| **Where the HTML goes** | Divi Code module. Section and row fullwidth, gutter 1, zero padding, page title hidden (see company-and-rules, Divi rules). Paste the file **contents**, not the path. |
| **If the live URL differs from the slug** | Fix the WordPress slug to match, or change the WPCode conditional and the schema `mainEntityOfPage` to the live URL. A mismatch silently disables the schema. |
| **Schema** | Paste the file **contents** into a WPCode HTML snippet with the settings below. |
| **Generated image** (if stage 7 ran) | Filename, **alt text**, caption, mode (diagram / realistic), and the figure snippet. Never without the alt text. |
| **Ledger summary** | Confirmed / confirmed-via-tier-2 / corrected / dropped counts, which numbers are estimates, and which NEC quotes rest on tier-2 sources. |
| **Humanizer score** | The content-humanizer scorer result after stage 4b (target 80+). |
| **Information gain** | The one thing this post has that competitors do not. |

Then the clipboard: post HTML first (`pbcopy < file`), schema on request.

## Chat delivery format (approved by Max, Nov 2026)

The full delivery block above goes into `OUTPUTS/<slug>-DELIVERY.md`. The chat message stays short and paste-ready, in this order, one turn per step:

1. **Delivery turn.** One line saying it's ready to publish and the post HTML is on the clipboard (`pbcopy` the post first). Then a compact two-column table with only the fields Max pastes into WordPress: WP title, slug, SEO title, focus keyword, meta (with char count), tags, publish date. Link the DELIVERY.md and schema file. Then 3-5 bullets: how prices are handled, the information gain, the ledger counts in one line, any re-check date. Then the GBP companion: image path, the post text in a fenced code block (never a blockquote), and one line with post type, button, URL and compliance.
2. **"html on clip"**: re-run `pbcopy < <slug>-post.html`, confirm in one line.
3. **"schema"**: `pbcopy < <slug>-schema.txt`, then the WPCode settings as four bullets (snippet name, type, insertion, conditional URL in backticks) and the date reminder.
4. **"gbp"**: the GBP text in a code block, the image path, and the settings line.

Never paste the post HTML or schema JSON into chat. No preamble, no recap of the pipeline.

## WPCode settings for the schema

- Snippet name: `Schema - [Post Title] Blog Post`
- Snippet type: HTML Snippet
- Insertion: Auto Insert, Site Wide Footer
- Conditional logic: Page URL **is exactly** `https://client.example/blog/[slug]/`
- Publish the post first so the URL exists, then activate. Validate at https://validator.schema.org/.

## SEO title patterns

`[Focus Keyword] [Modifier] [Location] [Year]` or `[Focus Keyword] [Location]: [Year] [Modifier]`

Good: `Hot Tub Wiring Cost Portland: 2026 Install Guide` (48) / `Sauna Wiring Cost in Portland: 2026 Guide` (41) / `Federal Pacific & Zinsco Panel Replacement Portland 2026` (56)

Washington posts use "Vancouver WA", not Portland.

## Meta description pattern

`[Topic] [Location]: $[range]. [Hook]? [Differentiator]. Call (503) 555-0100.`

Good (154): `Hot tub wiring Portland: $700-$3,400 installed. Oregon's 28-inch bonding rule, 50A GFCI, permits filed for you. Same-week scheduling. Call (503) 555-0100.`

## Companion GBP post (always, right after delivery)

Follow the `example-electric-gbp-post` skill. Pass Google review first time:

- No phone number in body ("tap Call"), no URLs ("tap Learn More"), no prices unless Offer post
- No superlatives, no em dashes, no closing signature, no hashtags
- No "Master Electrician", no "Authorized Dealer"
- First bold line is the headline, no emoji
- One CTA at the end pointing at Learn More
- 250-400 chars sweet spot, 1,500 max
- Button URL = the new post URL
- Image (default): branded card per `reference/images.md`; real shoot photo as the alternative. Never AI people. Any code claim on the card is checked against the ledger like body copy.

Deliver as: bold headline + body, then settings table (post type, button, URL, photo), then compliance checkmarks.
