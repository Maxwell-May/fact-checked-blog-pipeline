# Example Electric content pipeline: architecture overview

A multi-agent, evidence-gated content system built on Claude Code for a licensed electrical contractor's SEO retainer. It turns a Search Console gap into a published, code-accurate, locally specific guide with a verifiable audit trail, and it exists because single-agent generation shipped errors that a human reviewer did not catch.

## Design goals

1. **No claim without a source.** Every factual sentence in a post traces to a ledger row with a primary-source URL and a verbatim quote.
2. **Separation of duties.** The agent that researches does not verify. The agent that writes does not audit. Adversarial checking is a role, not a step in the writer's checklist.
3. **Machines check what machines can check.** Encoding, banned phrases, meta lengths, schema validity, FAQ parity, link counts, word count: scripted, deterministic, blocking.
4. **Graceful degradation.** Ahrefs API when the plan allows; Search Console export when it does not. The output names its data source and window.
5. **Domain rules are data, not vibes.** Oregon amends the NEC. The pipeline reads the amendment table as a rendered page because text extraction loses the underline that marks what changed. That single rule fixed a live misattribution.

## Stages

| # | Stage | Actor | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | Intake | Orchestrator | user request | topic, jurisdiction, slug, work dir | |
| 1 | Keyword and gap data | Orchestrator + Ahrefs MCP (fallback `gsc_gaps.py`) | GSC project / export | ranked clusters, cannibalization check, data window | evidence stated |
| 2 | Research | 2 subagents in parallel (code/regulation; cost/permit/utility/local) | topic, questions, standards file | two claim ledgers | |
| 3 | Claim check | 1 adversarial subagent + `check_ledger.py` | both ledgers | checked ledger: CONFIRMED / CORRECTED / DROPPED / ESTIMATE | **blocking** |
| 4 | Write | Orchestrator | checked ledger, template | `[slug]-post.html`, `[slug]-schema.txt` | |
| 4b | Humanize | `content-humanizer` skill (Mode 1 + 2), facts frozen | draft body | de-AI'd draft, humanity score | score printed again by lint, warns under 80 |
| 5 | Lint | `lint_post.py` | both files | FAIL / WARN / CLEAN | **blocking** |
| 6 | Audit | 1 subagent (E-E-A-T, GEO, voice, conversion) | files + checked ledger | ranked findings with replacement text; SHIP verdict | **blocking** |
| 7 | Image (optional) | Higgsfield `nano_banana_pro` | ledger values | diagram or photoreal illustration, no people, **shipped with alt text and caption**; branded GBP card | render checked, alt text present |
| 8 | Deliver | Orchestrator | everything | delivery table, ledger counts, estimates, information gain | |
| 9 | GBP companion | Orchestrator | post URL, ledger | Google Business Profile post, compliance-checked | |

## Artifacts per post

```
outputs/
  ledgers/<slug>/code.md          # researcher-code ledger
  ledgers/<slug>/local.md         # researcher-local ledger
  ledgers/<slug>/checked.md       # claim-checker output (the source of truth for the post)
  <slug>-post.html                # Divi Code module content
  <slug>-schema.txt               # WPCode snippet (pure <script>)
  branding-tool/upload-ready/<slug>-gbp.png
```

## The claim ledger

```
| # | Claim | Jurisdiction | Source URL | Verbatim quote / page image | Status | Verified on | Check result | Checker note |
```

Statuses move in one direction: `UNVERIFIED -> (never used)`, `SECONDARY -> CONFIRMED only after a primary source is found`, `ESTIMATE` stays ESTIMATE and must be labelled in prose. The gate script refuses to open if any row is UNVERIFIED, CONFLICT, or lacks a source.

## What the lint enforces (all learned from a shipped defect)

Non-ASCII characters; em dashes; emojis; "free"; "Master Electrician"; "Authorized Dealer"; the retired phone number; `<h1>`; CDN icon scripts; per-post sticky bar; founder blockquote; placeholder image src; the dead permit-agency name and dead CCB URL; missing Last-updated line, trust bar, both license numbers, FAQ (5-7), Sources, final CTA; fewer than 2 primary-source links or 3 internal links; word count; SEO title over 60; meta over 160 or not ending in the phone CTA; excerpt length; schema not pure `<script>`; invalid JSON; schema FAQ text not on the page verbatim; `dateModified` not equal to the visible date; off-domain schema image; slug mismatch.

## Failure modes it was built against

| Shipped or nearly shipped | Root cause | Control |
|---|---|---|
| "Oregon adds this sentence" about a spa bonding rule; Oregon added two words | PDF read as text, underline lost | Table 1-E rendered as image; checker re-renders |
| Cost table with unsourced ranges presented as fact | Writer verified its own numbers | ESTIMATE status, label requirement, auditor check |
| Report compared 6-month page totals to 3-month totals | Windows not surfaced | Every output states its window |
| Flyer rendered with a logo file carrying the old phone number | Asset not audited | Lint bans the number; rules name the file |
| Blank image box on a live post | Placeholder src | Lint |
| Recommended title rewrites to fix a sub-1% CTR at position 1-3 | Impressions treated as human | CTR reality check in `gsc_gaps.py`; standing rule |

## Reviews applied

Before install the package was reviewed three ways: a fresh-agent dry run (10 findings: relative paths, unnamed tool prefixes, gate parsing, ESTIMATE semantics, question fallback, GBP default, lint length band, missing delivery fields), an Archer code audit (17 findings, headline: both gates failed open on malformed input; the schema was never scanned for banned phrases; no prompt-injection guard in web-reading agents), and a skill-authoring review against the writing-skills and Maestro standards (11 recommendations, headline: invisible to the router, token cost, hardcoded plugin path). All blocking and high items were applied and re-tested; Archer's adversarial fixtures are kept as a regression suite in `scripts/test_fixtures.sh`.

## Tooling

Claude Code as orchestrator; the `content-humanizer` plugin for the de-AI pass; `general-purpose` subagents via the Agent tool; Ahrefs MCP (GSC-connected project <project-id>); Higgsfield MCP for image generation; poppler (`pdftoppm`, `pdftotext`) for amendment tables; Chrome headless for GBP card rendering; Python 3 stdlib for lint and gates.

## Running it

Invoke the `example-electric-blog` skill with a topic or "pick the next topic". The skill file is the runbook; `README-PIPELINE.md` is this overview.
