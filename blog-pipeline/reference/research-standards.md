# Research standards and verified facts

Facts here carry the date they were last verified. Anything older than 90 days gets re-verified before it goes in a post. Anything not here gets verified from scratch. **A ledger row may cite this file only alongside the original URL**; the gate rejects a Source cell that names only this file, because the checker cannot open a memory.

## Source hierarchy

1. **Primary, binding:** Oregon BCD (Table 1-E, OESC adoption page), ORS / OAR (oregon.public.law), Washington L&I / WAC, NFPA 70 text, Portland PP&D fee schedules and permit pages, county permit portals, PGE / Clark Public Utilities / NW Natural tariffs and program pages, Energy Trust of Oregon, IRS, manufacturer installation manuals.
2. **Primary, contextual:** NAHB, IAEI, EC&M, Mike Holt (for NEC interpretation only, never for Oregon adoption status).
3. **Never a source:** contractor blogs, lead-gen sites, permit-calculator sites, AI summaries, Gemini reports, this skill's own memory. They are lead lists.

## The Table 1-E rule (CRITICAL)

Oregon does not adopt the NEC wholesale. Table 1-E lists every amendment. Language not in the table is unamended.

**Read the table as a page image, never as extracted text.** Oregon marks additions with underline and deletions with strikethrough. `pdftotext` strips both, so the text dump shows the amended section but cannot tell you which words Oregon changed. That produced a published claim that "Oregon adds this sentence" when Oregon added two words to an NEC sentence. Use `scripts/render_table1e.sh <section>` which renders the matching page to PNG and prints the file path; then Read the image.

Current table: **2026 OESC Table 1-E, effective Oct 1, 2026**, based on the 2026 NEC (verified on oregon.gov/bcd, Oct 11, 2026). URL: https://www.oregon.gov/bcd/codes-stand/Documents/26oesc-table1-E.pdf. Superseded: 2023 OESC table (23oesc-table1-E.pdf). Under OAR 918-305-0020 a job permitted before Oct 1, 2026 may still be under the 2023 OESC.

**2026 OESC:** adopted and in effect Oct 1, 2026 (verified Oct 11, 2026). Older 2023-table rows in this file are leads only: re-render the 2026 table before using them, because section numbers and Oregon amendments changed (e.g. 210.12 exceptions). https://www.oregon.gov/bcd/codes-stand/pages/oesc-adoption.aspx

### Verified Oregon amendments

Rows marked "page image" were read from the rendered PDF page. Rows marked "text dump" or "Aug 2026" without "page image" were read from extracted text and **must be rendered with `scripts/render_table1e.sh` before the claim is used**, however close the date is.

| Section | Oregon status | Verified |
|---|---|---|
| 210.8(F) outdoor HVAC GFCI | Exception expired Sept 1, 2026 nationally; no extension found. Oregon's adoption of 210.8(F) itself must be confirmed on the page image before any claim. | Sept 3, 2026 (expiry); adoption status NOT yet confirmed |
| 210.12(B) | Exception No. 2 applies; Exceptions 1-4 exist | Aug 2026 |
| 230.70(A)(1) | Oregon ADDS an exception: on replacement of a service panel or meter base the panel and service disconnect may stay at the existing location IF the existing conductors have ampacity for the load or the conduit can take ones that do, AND 110.26/240.24 are met, with the working space DEPTH at 0-150 V to ground reduced to 30 in. for pre-July 1 1978 installations. Conjunctive: all conditions must hold. 30 in. is a DEPTH allowance, never a width. | Sept 8, 2026, page image |
| 230.24, 230.28, 230.42, 230.79 | Not in Table 1-E; unamended NEC applies in Oregon (confirmed by rendering Article 230 with --all) | Sept 8, 2026, page image |
| Article 220, Article 310 | Not in Table 1-E at all; NEC load-calculation and conductor rules apply in Oregon unchanged | Sept 8, 2026, page image |
| 210.12(D) | Not adopted | Aug 2026 |
| 210.12(E) | Oregon's own Exception No. 2: "Replacement or upgrading of a service or panelboard shall not require that existing circuits be protected by AFCI devices." Exception No. 1 covers extensions and modifications. A whole-house rewire DOES require AFCI (base rule; neither exception applies). | Sept 8, 2026, page image |
| 225.41, 225.42 | Not adopted | Aug 2026 (text dump; re-confirm on image before citing) |
| 230.67, 230.85 | Not adopted by the State of Oregon. Also 215.18 and 225.42 (surge) and 225.41 (emergency disconnect). WASHINGTON IS THE INVERSE: WAC 296-46B-230(11) requires an emergency disconnect when service equipment supplying a one- or two-family dwelling is replaced. Never let these share a sentence without naming both states. | Sept 8, 2026, page image |
| 406.4(D)(4) | Not adopted. Replacing a receptacle does not trigger AFCI. | Sept 8, 2026, page image |
| 625.54, 630.8 | Not adopted (GFCI for personnel) | Sept 4, 2026, page image |
| 680.4 Inspections after installation | Not adopted | Sept 4, 2026, page image |
| 680.21(D) Pool pump motor replacement | Not adopted | Sept 4, 2026, page image |
| 680.42(B)(4) spa bonding rim rule | NEC text retained; Oregon inserts the two words **"or deck"** into the nonconductive-steps sentence. Nothing else in (4) is Oregon's. | Sept 4, 2026, page image |
| 682.15(B) piers GFPE | 30 mA struck, 100 mA added | Sept 4, 2026, page image |
| Table 300.5 burial depths | Not amended | Aug 2026 |

**Washington is a separate jurisdiction.** WA runs the 2023 NEC under WAC 296-46B with its own amendments; 2026 edition effective Dec 31, 2026 (verify before citing). Never apply an Oregon amendment to a Vancouver or Clark County post.

## Verified facts with dates

| Fact | Value | Verified |
|---|---|---|
| Portland permitting agency | Portland Permitting & Development (PP&D), replaced BDS June 1, 2024. Link https://www.portland.gov/ppd | Aug 2026 |
| Portland electrical fee schedule | Effective July 10, 2026. First branch circuit without service/feeder $174.00; each additional $21.00; 200A service/feeder $212.00; plan review 25%. **Client rule: link the schedule, do not quote exact fees in posts** unless the user explicitly approves quoting for that post. | Sept 3, 2026, PDF |
| Oregon state permit surcharge | 12% of the permit fee, electrical services expressly included. Source: Oregon BCD surcharge backgrounder, which cites ORS 455.210(3)(c) and ORS 455.020(4). Do NOT attribute it to ORS 455.220 without a source that says so. | Sept 8, 2026, corrected |
| Homeowner electrical permits | ORS 479.540 exempts the owner from the electrical LICENSE on residential property they or an immediate family member own and do not intend to sell, exchange, lease or rent. It is not a permit exemption: ORS 479.540 keeps that to maintenance and excludes substantial alterations. In the City of Portland the homeowner permit covers lights, outlets, switches and circuits, not a service change. | Sept 8, 2026 |
| Square-foot packages vs minor labels | OAR 918-309 places NO amperage cap on residential square-foot wiring packages; OAR 918-309-0030 says the residential fee "covers services, feeders and all branch circuits" and Portland's schedule says "Service included" with no qualifier. The 200 A / 150 V limit belongs to MINOR LABELS under OAR 918-309-0220(7)(c), which also bars complete replacement of a service. | Sept 8, 2026, corrected |
| PGE residential Schedule 7 | About 11.4 cents/kWh early 2026; about 5% increase effective April 1, 2026 | Sept 3, 2026, secondary; confirm on portlandgeneral.com before quoting |
| NEC 680.13 spa disconnect | Readily accessible, within sight (50 ft), at least 5 ft horizontally from inside walls unless a permanent barrier gives a 5 ft reach path | Sept 3, 2026 |
| NEC 680.42(B) bonding exemption | Four conditions: listed self-contained aboveground; not indoor-only; per manufacturer on or above grade; rim 28 in above perimeter surfaces within 30 in | Sept 3, 2026 |
| 50A spa circuit conductor | 6 AWG copper (65A at 75C) to roughly 75 ft; 4 AWG beyond for voltage drop | Sept 3, 2026, secondary |
| Saunas | NEC Article 422, NOT 680 | standing |
| Hot tubs / spas | NEC Article 680 | standing |
| Federal 25C | Expired Dec 31, 2025 | Aug 2026 |
| Federal 30C EV charger credit | Expired June 30, 2026 | Aug 2026 |
| Oregon Clean Vehicle Rebate | Purchases/leases after Nov 4, 2026 not eligible | Aug 2026, re-verify |
| Oregon HOMES / HEAR | HEAR income-qualified to 150% AMI; verify current status | Aug 2026 |
| Oregon CCB lookup URL | https://www.oregon.gov/ccb/pages/default.aspx (ccb.oregon.gov form is dead) | standing |
| FAQ rich results | Deprecated May 7, 2026. Keep FAQPage markup; it earns no SERP feature. | Aug 2026 |
| Google generative AI guidance | May 15, 2026: no special optimizations, no llms.txt needed | Aug 2026 |
| March 2026 core update | Page-level authority, composite CWV, information-gain signal | Aug 2026 |
| Thumbtack lead payload | Fires `NegotiationCreatedV4` once at contact; no update event; `leadPrice` is a string; sales tax by business address (Oregon = $0.00) | Aug 2026 |

| PGE equipment ownership | PGE owns the meter, the service wire to the weatherhead, and the entry point of an underground meter base. The owner owns the meter base, weatherhead, conduit and wiring from the weatherhead onward. Source: portlandgeneral.com residential rights and responsibilities. | Sept 8, 2026 |
| PGE service upgrade rules | PGE Electric Service Requirements (ESR), January 2026 book. Defines a service upgrade as any service "altered, modified, replaced, or updated"; requires BOTH a local permit/inspection AND a PGE inspection before reconnection when amperage increases or service equipment is relocated/replaced; requires the meter socket, weatherhead AND their locations brought to current requirements on an upgrade; residential ceiling of 320 A continuous before CT metering is required. | Sept 8, 2026 |
| PGE reconnect gate | "Your meter base must have the approval sticker attached from the city/county before we can connect your service." PGE publishes conflicting lead times (5-10 business days vs 2-4 weeks) covering different scopes: cite roughly one to four weeks and link both. PGE publishes NO fee and NO outage duration for a planned residential disconnect; never write "PGE does not charge" or a duration. | Sept 8, 2026 |
| PG&E vs PGE trap | Searches for "PGE underground conversion tariff" return **Pacific Gas & Electric (California, pge.com)** Rule 20/Rule 16. That is a different utility. Portland General Electric is portlandgeneral.com. Never let a pge.com source into an Oregon post. | Sept 8, 2026 |
| Energy Trust incentives | The 2026 Residential Incentive Information Sheet lists NO incentive for an electrical panel or service upgrade. The PDF contains an Oregon sheet and a Washington sheet in one file; attribute hits to the correct half. | Sept 8, 2026 |
| Portland reconnection after vacancy | PCC **26.06.070** (Electrical Reconnections), NOT 26.04: inspection required before power is reconnected to a building vacant with power off for six months. | Sept 8, 2026, corrected |
| Portland plan review thresholds | Services/feeders 600 A or over, or 400 A+ where available fault current exceeds 10,000 A at 150 V or less to ground. Ordinary 200 A residential work is below both. | Sept 8, 2026 |
| Portland housing age | About six in ten Portland homes built before 1980 (ACS 2024 1-year, Table B25034). Margin of error is large; do NOT print the raw count. NOTHING ties housing age to service amperage: never claim a share of homes run 60A or 100A. | Sept 8, 2026 |

## Data windows

GSC exports are windowed. A "Last 3 months" export and a "Last 6 months" export give different page and query totals for the same site. Every table in a post or report states its window. Never compare a 6-month total to a 3-month one. Query-level numbers decay: a term at position 1 with about a thousand six-month impressions was in single digits in the following 3-month window. Re-pull before citing.

## AI-surface caveat

Non-brand CTR at positions 1-3 on this site is a fraction of a percent (expected 15-28%). Hundreds of non-brand queries rank top 10 with zero clicks. Desktop carries far more impressions than mobile at a much lower CTR. Impressions are largely AI Mode fan-out, not people. Do not recommend title or meta rewrites to "reclaim CTR", and do not sell impressions as wins.
