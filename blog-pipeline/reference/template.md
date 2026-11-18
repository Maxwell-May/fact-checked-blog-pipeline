# Example Electric blog template (v3)

Canonical design system for every post. Do not deviate without explicit approval. All icons are inline SVG (no CDN). No sticky bar. No `<h1>`. No founder blockquote.

## Style block

Paste at the top of `[slug]-post.html`, after the meta comment, before `<div class="ea-post">`.

```html
<style>
.ea-post {
  --ea-navy: #1a1a2e;
  --ea-navy-light: #2d3561;
  --ea-orange: #f5a623;
  --ea-orange-soft: #fdf8f0;
  --ea-bg: #f4f6f9;
  --ea-border: #dde1e7;
  --ea-text: #2a2d3a;
  --ea-muted: #6b7280;
  --ea-success: #2e7d32;
  --ea-danger: #c62828;
  --ea-radius: 10px;
  --ea-shadow: 0 4px 20px rgba(26, 26, 46, 0.08);
  --ea-shadow-lg: 0 12px 40px rgba(26, 26, 46, 0.12);
  font-family: inherit; color: var(--ea-text); line-height: 1.7; font-size: 17px;
}
.ea-post p { margin: 0 0 18px; }
.ea-post a { color: var(--ea-navy-light); text-decoration: underline; text-decoration-thickness: 1.5px; text-underline-offset: 3px; }
.ea-post a:hover { color: var(--ea-orange); }

.ea-hero-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 24px 0 32px; }
.ea-stat { background: linear-gradient(135deg, var(--ea-navy) 0%, var(--ea-navy-light) 100%); color: white; padding: 18px 14px; border-radius: var(--ea-radius); text-align: center; box-shadow: var(--ea-shadow); }
.ea-stat-value { font-size: 24px; font-weight: 800; color: var(--ea-orange); display: block; line-height: 1.1; margin-bottom: 4px; }
.ea-stat-label { font-size: 12px; text-transform: uppercase; letter-spacing: 0.6px; opacity: 0.85; font-weight: 600; }
@media (max-width: 600px) { .ea-hero-stats { grid-template-columns: repeat(2, 1fr); gap: 10px; } .ea-stat-value { font-size: 20px; } }

.ea-trust-bar { background: var(--ea-bg); border: 1px solid var(--ea-border); border-left: 4px solid var(--ea-orange); border-radius: var(--ea-radius); padding: 14px 20px; margin: 24px 0; display: flex; flex-wrap: wrap; gap: 18px; align-items: center; font-size: 14px; font-weight: 600; }
.ea-trust-bar span { display: inline-flex; align-items: center; gap: 6px; }
.ea-trust-bar strong { color: var(--ea-navy); }

.ea-post h2 { font-size: 28px; font-weight: 800; color: var(--ea-navy); margin: 48px 0 16px; line-height: 1.25; position: relative; padding-bottom: 10px; }
.ea-post h2::after { content: ""; display: block; width: 60px; height: 3px; background: var(--ea-orange); position: absolute; bottom: 0; left: 0; }
.ea-post h3 { font-size: 21px; font-weight: 700; color: var(--ea-navy); margin: 32px 0 12px; }
@media (max-width: 600px) { .ea-post h2 { font-size: 24px; } .ea-post h3 { font-size: 19px; } }

.ea-post table { width: 100%; border-collapse: separate; border-spacing: 0; margin: 28px 0; font-size: 15px; background: white; border-radius: var(--ea-radius); overflow: hidden; box-shadow: var(--ea-shadow); }
.ea-post table thead tr { background: linear-gradient(135deg, var(--ea-navy) 0%, var(--ea-navy-light) 100%) !important; color: white !important; }
.ea-post table th { color: white !important; text-align: left; padding: 14px 16px; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; border: none; }
.ea-post table td { padding: 14px 16px; border: none; border-bottom: 1px solid var(--ea-border); vertical-align: top; }
.ea-post table tbody tr:nth-of-type(even) { background-color: #fafbfc; }
.ea-post table tbody tr:hover { background-color: var(--ea-orange-soft); }
.ea-post table tbody tr:last-of-type td { border-bottom: none; }
.ea-table-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 28px 0; border-radius: var(--ea-radius); box-shadow: var(--ea-shadow); }
.ea-table-wrap table { margin: 0; box-shadow: none; }

.ea-compare { display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; margin: 28px 0; }
.ea-card { background: white; border: 2px solid var(--ea-border); border-radius: var(--ea-radius); padding: 22px; position: relative; transition: transform 0.2s, box-shadow 0.2s; }
.ea-card:hover { transform: translateY(-2px); box-shadow: var(--ea-shadow-lg); }
.ea-card-tag { display: inline-block; background: var(--ea-orange-soft); color: var(--ea-navy); padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 10px; }
.ea-card-tag.heavy { background: var(--ea-navy); color: white; }
.ea-card h4 { font-size: 18px; font-weight: 700; color: var(--ea-navy); margin: 0 0 10px; }
.ea-card-spec { font-size: 13px; color: var(--ea-muted); margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--ea-border); }
.ea-card-spec strong { color: var(--ea-navy); }
@media (max-width: 600px) { .ea-compare { grid-template-columns: 1fr; } }

.ea-callout { background: var(--ea-orange-soft); border: 1px solid #f0d59c; border-left: 4px solid var(--ea-orange); border-radius: var(--ea-radius); padding: 18px 22px; margin: 28px 0; }
.ea-callout-title { font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: var(--ea-orange); margin-bottom: 6px; }
.ea-callout p:last-child { margin-bottom: 0; }
.ea-callout.warn { background: #fff5f5; border-color: #fcc; border-left-color: var(--ea-danger); }
.ea-callout.warn .ea-callout-title { color: var(--ea-danger); }

.ea-cta-inline { background: linear-gradient(135deg, var(--ea-navy) 0%, var(--ea-navy-light) 100%); color: white; padding: 24px 28px; border-radius: var(--ea-radius); margin: 36px 0; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 18px; box-shadow: var(--ea-shadow); }
.ea-cta-inline-text { flex: 1; min-width: 220px; }
.ea-cta-inline h4 { color: white; font-size: 19px; font-weight: 700; margin: 0 0 4px; }
.ea-cta-inline p { color: rgba(255,255,255,0.85); margin: 0; font-size: 14px; }
.ea-btn { display: inline-block; background: var(--ea-orange); color: var(--ea-navy) !important; padding: 14px 28px; border-radius: 8px; font-weight: 800; text-decoration: none !important; font-size: 16px; transition: transform 0.15s, box-shadow 0.2s; box-shadow: 0 4px 14px rgba(245, 166, 35, 0.4); white-space: nowrap; }
.ea-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(245, 166, 35, 0.55); color: var(--ea-navy) !important; }


.ea-faq { margin: 24px 0; }
.ea-faq details { background: white; border: 1px solid var(--ea-border); border-radius: var(--ea-radius); margin-bottom: 12px; overflow: hidden; transition: box-shadow 0.2s; }
.ea-faq details[open] { box-shadow: var(--ea-shadow); border-color: var(--ea-orange); }
.ea-faq summary { cursor: pointer; padding: 18px 22px; font-weight: 700; color: var(--ea-navy); font-size: 16px; list-style: none; position: relative; padding-right: 50px; }
.ea-faq summary::-webkit-details-marker { display: none; }
.ea-faq summary::after { content: "+"; position: absolute; right: 22px; top: 50%; transform: translateY(-50%); font-size: 24px; color: var(--ea-orange); font-weight: 400; transition: transform 0.2s; }
.ea-faq details[open] summary::after { content: "\2212"; }
.ea-faq summary:hover { background: var(--ea-orange-soft); }
.ea-faq-answer { padding: 0 22px 20px; color: var(--ea-text); }
.ea-faq-answer p:last-child { margin-bottom: 0; }

.ea-final-cta { background: linear-gradient(135deg, var(--ea-navy) 0%, var(--ea-navy-light) 100%); color: white; padding: 44px 36px; border-radius: var(--ea-radius); margin: 48px 0 24px; text-align: center; position: relative; overflow: hidden; }
.ea-final-cta::before { content: ""; position: absolute; top: -40px; right: -40px; width: 200px; height: 200px; background: var(--ea-orange); border-radius: 50%; opacity: 0.12; }
.ea-final-cta::after { content: ""; position: absolute; bottom: -60px; left: -60px; width: 240px; height: 240px; background: var(--ea-orange); border-radius: 50%; opacity: 0.08; }
.ea-final-cta h2 { color: white; margin: 0 0 12px; padding: 0; }
.ea-final-cta h2::after { background: var(--ea-orange); margin: 14px auto 0; left: 50%; transform: translateX(-50%); }
.ea-final-cta p { color: rgba(255,255,255,0.9); max-width: 640px; margin: 0 auto 24px; font-size: 16px; }
.ea-final-cta-btns { display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; position: relative; z-index: 1; }
.ea-btn-secondary { display: inline-block; background: transparent; color: white !important; padding: 14px 28px; border-radius: 8px; font-weight: 700; text-decoration: none !important; font-size: 16px; border: 2px solid rgba(255,255,255,0.4); transition: all 0.2s; }
.ea-btn-secondary:hover { background: rgba(255,255,255,0.1); border-color: white; color: white !important; }


.ea-post ul { margin: 16px 0 24px 24px; padding: 0; }
.ea-post ul li { margin-bottom: 10px; padding-left: 4px; }
.ea-post ul li::marker { color: var(--ea-orange); font-weight: 700; }
/* v3 additions */
.ea-post .ea-ico { width: 1em; height: 1em; fill: currentColor; vertical-align: -0.125em; flex-shrink: 0; }
.ea-trust-bar .ea-ico { width: 18px; height: 18px; color: var(--ea-orange); margin-right: 4px; }
.ea-btn .ea-ico { width: 18px; height: 18px; color: var(--ea-navy); margin-right: 6px; vertical-align: -3px; }
.ea-btn-secondary .ea-ico { width: 18px; height: 18px; color: #fff; margin-right: 6px; vertical-align: -3px; }
.ea-callout-title .ea-ico { width: 14px; height: 14px; vertical-align: -2px; margin-right: 4px; }
.ea-updated { font-size: 13px; color: var(--ea-muted); margin: 0 0 14px; }
.ea-toc { background: var(--ea-bg); border: 1px solid var(--ea-border); border-radius: var(--ea-radius); padding: 16px 22px; margin: 24px 0 32px; font-size: 15px; }
.ea-toc strong { display: block; color: var(--ea-navy); margin-bottom: 8px; font-size: 13px; text-transform: uppercase; letter-spacing: .6px; }
.ea-toc ol { margin: 0 0 0 20px; padding: 0; } .ea-toc li { margin: 4px 0; }
.ea-sources { font-size: 14px; color: var(--ea-muted); border-top: 1px solid var(--ea-border); padding-top: 16px; margin-top: 36px; }
.ea-sources ol { margin: 8px 0 0 20px; } .ea-sources li { margin: 4px 0; }
.ea-faq details[open] summary::after { content: "\2212"; }
/* Divi override: scope !important to direct children so CTA white text survives */
.ea-post > p { color: var(--ea-text) !important; }
.ea-final-cta p, .ea-final-cta h2 { color: #fff !important; }
.ea-cta-inline p, .ea-cta-inline h4 { color: #fff !important; }
.ea-post figure { margin: 28px 0; } .ea-post figure img { width: 100%; height: auto; border-radius: var(--ea-radius); display: block; }
.ea-post figcaption { font-size: 13px; color: var(--ea-muted); margin-top: 8px; }
</style>
```

## Inline SVG icon set

Ionicons 7.4.0 paths, embedded. Copy the exact tag. Outline icons carry their own stroke attributes; the wrapper CSS sets `fill: currentColor`. Always `aria-hidden="true"` on decorative icons.

| Use | Name | Tag |
|---|---|---|
| Phone / call CTA | `call` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M391 480c-19.52 0-46.94-7.06-88-30-49.93-28-88.55-53.85-138.21-103.38C116.91 298.77 93.61 267.79 61 208.45c-36.84-67-30.56-102.12-23.54-117.13C45.82 73.38 58.16 62.65 74.11 52a176.3 176.3 0 0128.64-15.2c1-.43 1.93-.84 2.76-1.21 4.95-2.23 12.45-5.6 21.95-2 6.34 2.38 12 7.25 20.86 16 18.17 17.92 43 57.83 52.16 77.43 6.15 13.21 10.22 21.93 10.23 31.71 0 11.45-5.76 20.28-12.75 29.81-1.31 1.79-2.61 3.5-3.87 5.16-7.61 10-9.28 12.89-8.18 18.05 2.23 10.37 18.86 41.24 46.19 68.51s57.31 42.85 67.72 45.07c5.38 1.15 8.33-.59 18.65-8.47 1.48-1.13 3-2.3 4.59-3.47 10.66-7.93 19.08-13.54 30.26-13.54h.06c9.73 0 18.06 4.22 31.86 11.18 18 9.08 59.11 33.59 77.14 51.78 8.77 8.84 13.66 14.48 16.05 20.81 3.6 9.53.21 17-2 22-.37.83-.78 1.74-1.21 2.75a176.49 176.49 0 01-15.29 28.58c-10.63 15.9-21.4 28.21-39.38 36.58A67.42 67.42 0 01391 480z"/></svg>` |
| Licensed / electrical | `flash-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M315.27 33L96 304h128l-31.51 173.23a2.36 2.36 0 002.33 2.77h0a2.36 2.36 0 001.89-.95L416 208H288l31.66-173.25a2.45 2.45 0 00-2.44-2.75h0a2.42 2.42 0 00-1.95 1z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/></svg>` |
| Veteran-owned | `ribbon-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><circle cx="256" cy="160" r="128" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path d="M143.65 227.82L48 400l86.86-.42a16 16 0 0113.82 7.8L192 480l88.33-194.32" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path d="M366.54 224L464 400l-86.86-.42a16 16 0 00-13.82 7.8L320 480l-64-140.8" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><circle cx="256" cy="160" r="64" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/></svg>` |
| 24/7 / time | `time-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M256 64C150 64 64 150 64 256s86 192 192 192 192-86 192-192S362 64 256 64z" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="32"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M256 128v144h96"/></svg>` |
| Permits / paperwork | `document-text-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M416 221.25V416a48 48 0 01-48 48H144a48 48 0 01-48-48V96a48 48 0 0148-48h98.75a32 32 0 0122.62 9.37l141.26 141.26a32 32 0 019.37 22.62z" fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="32"/><path d="M256 56v120a32 32 0 0032 32h120M176 288h160M176 368h160" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/></svg>` |
| Service area | `location-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M256 48c-79.5 0-144 61.39-144 137 0 87 96 224.87 131.25 272.49a15.77 15.77 0 0025.5 0C304 409.89 400 272.07 400 185c0-75.61-64.5-137-144-137z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><circle cx="256" cy="192" r="48" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/></svg>` |
| Warning / hazard | `warning-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M85.57 446.25h340.86a32 32 0 0028.17-47.17L284.18 82.58c-12.09-22.44-44.27-22.44-56.36 0L57.4 399.08a32 32 0 0028.17 47.17z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path d="M250.26 195.39l5.74 122 5.73-121.95a5.74 5.74 0 00-5.79-6h0a5.74 5.74 0 00-5.68 5.95z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path d="M256 397.25a20 20 0 1120-20 20 20 0 01-20 20z"/></svg>` |
| Code reference / info | `information-circle-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M248 64C146.39 64 64 146.39 64 248s82.39 184 184 184 184-82.39 184-184S349.61 64 248 64z" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="32"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M220 220h32v116"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-miterlimit="10" stroke-width="32" d="M208 340h88"/><path d="M248 130a26 26 0 1026 26 26 26 0 00-26-26z"/></svg>` |
| Verified | `checkmark-circle-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M448 256c0-106-86-192-192-192S64 150 64 256s86 192 192 192 192-86 192-192z" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="32"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M352 176L217.6 336 160 272"/></svg>` |
| Rating | `star` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M394 480a16 16 0 01-9.39-3L256 383.76 127.39 477a16 16 0 01-24.55-18.08L153 310.35 23 221.2a16 16 0 019-29.2h160.38l48.4-148.95a16 16 0 0130.44 0l48.4 149H480a16 16 0 019.05 29.2L359 310.35l50.13 148.53A16 16 0 01394 480z"/></svg>` |
| Scheduling | `calendar-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><rect fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="32" x="48" y="80" width="416" height="384" rx="48"/><circle cx="296" cy="232" r="24"/><circle cx="376" cy="232" r="24"/><circle cx="296" cy="312" r="24"/><circle cx="376" cy="312" r="24"/><circle cx="136" cy="312" r="24"/><circle cx="216" cy="312" r="24"/><circle cx="136" cy="392" r="24"/><circle cx="216" cy="392" r="24"/><circle cx="296" cy="392" r="24"/><path fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="32" stroke-linecap="round" d="M128 48v32M384 48v32"/><path fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="32" d="M464 160H48"/></svg>` |
| Pricing | `cash-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><rect x="32" y="80" width="448" height="256" rx="16" ry="16" transform="rotate(180 256 208)" fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="32"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M64 384h384M96 432h320"/><circle cx="256" cy="208" r="80" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path d="M480 160a80 80 0 01-80-80M32 160a80 80 0 0080-80M480 256a80 80 0 00-80 80M32 256a80 80 0 0180 80" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/></svg>` |
| Inspection | `search-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M221.09 64a157.09 157.09 0 10157.09 157.09A157.1 157.1 0 00221.09 64z" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="32"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-miterlimit="10" stroke-width="32" d="M338.29 338.29L448 448"/></svg>` |
| Residential | `home-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M80 212v236a16 16 0 0016 16h96V328a24 24 0 0124-24h80a24 24 0 0124 24v136h96a16 16 0 0016-16V212" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path d="M480 256L266.89 52c-5-5.28-16.69-5.34-21.78 0L32 256M400 179V64h-48v69" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/></svg>` |
| Quote / form | `clipboard-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M336 64h32a48 48 0 0148 48v320a48 48 0 01-48 48H144a48 48 0 01-48-48V112a48 48 0 0148-48h32" fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="32"/><rect x="176" y="32" width="160" height="64" rx="26.13" ry="26.13" fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="32"/></svg>` |
| Email | `mail-outline` | `<svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><rect x="48" y="96" width="416" height="320" rx="40" ry="40" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M112 160l144 112 144-112"/></svg>` |

## Required components

**Meta comment block** (top of file):
```html
<!--
  Title: [WP post title / H1]
  SEO Title: [Rank Math, max 60 chars]
  Slug: [slug]
  Focus keyword: [primary keyword]
  Meta description: [max 160 chars, ends with Call (503) 555-0100.]
  Excerpt: [50-70 words]
  Jurisdiction: [Oregon / Washington / both]
  Information gain: [the one thing competitors do not have]
  Ledger: [path to claim ledger used]
-->
```

**Last updated line** (first element inside `.ea-post`, must match schema `dateModified`):
```html
<p class="ea-updated">Last updated September 4, 2026</p>
```

**Hero stat row** (4 stats):
```html
<div class="ea-hero-stats">
  <div class="ea-stat"><span class="ea-stat-value">VALUE</span><span class="ea-stat-label">LABEL</span></div>
  <!-- 3 more -->
</div>
```

**Trust bar** (always both licenses):
```html
<div class="ea-trust-bar">
  <span><svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M315.27 33L96 304h128l-31.51 173.23a2.36 2.36 0 002.33 2.77h0a2.36 2.36 0 001.89-.95L416 208H288l31.66-173.25a2.45 2.45 0 00-2.44-2.75h0a2.42 2.42 0 00-1.95 1z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/></svg><strong>Licensed</strong> &middot; OR CCB# 000000 &middot; WA EXAMPLE000XX</span>
  <span><svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><circle cx="256" cy="160" r="128" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path d="M143.65 227.82L48 400l86.86-.42a16 16 0 0113.82 7.8L192 480l88.33-194.32" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path d="M366.54 224L464 400l-86.86-.42a16 16 0 00-13.82 7.8L320 480l-64-140.8" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><circle cx="256" cy="160" r="64" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/></svg><strong>Veteran-Owned</strong></span>
  <span><svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M256 64C150 64 64 150 64 256s86 192 192 192 192-86 192-192S362 64 256 64z" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="32"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M256 128v144h96"/></svg><strong>24/7</strong> Emergency</span>
  <span><svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M416 221.25V416a48 48 0 01-48 48H144a48 48 0 01-48-48V96a48 48 0 0148-48h98.75a32 32 0 0122.62 9.37l141.26 141.26a32 32 0 019.37 22.62z" fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="32"/><path d="M256 56v120a32 32 0 0032 32h120M176 288h160M176 368h160" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/></svg><strong>Permits</strong> Filed for You</span>
</div>
```

**Table of contents** (posts over ~1,500 words):
```html
<nav class="ea-toc" aria-label="Contents"><strong>In this guide</strong><ol>
  <li><a href="#cost">What it costs</a></li>
  <!-- one per H2, ids on the H2s -->
</ol></nav>
```

**Data table** (wrap for mobile scroll):
```html
<div class="ea-table-wrap"><table>
  <thead><tr><th>Col</th><th>Col</th></tr></thead>
  <tbody><tr><td>..</td><td>..</td></tr></tbody>
</table></div>
```

**Inline CTA** (1-2 per post):
```html
<div class="ea-cta-inline">
  <div class="ea-cta-inline-text"><h4>HOOK</h4><p>SUPPORTING LINE</p></div>
  <a href="tel:5035550100" class="ea-btn"><svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M391 480c-19.52 0-46.94-7.06-88-30-49.93-28-88.55-53.85-138.21-103.38C116.91 298.77 93.61 267.79 61 208.45c-36.84-67-30.56-102.12-23.54-117.13C45.82 73.38 58.16 62.65 74.11 52a176.3 176.3 0 0128.64-15.2c1-.43 1.93-.84 2.76-1.21 4.95-2.23 12.45-5.6 21.95-2 6.34 2.38 12 7.25 20.86 16 18.17 17.92 43 57.83 52.16 77.43 6.15 13.21 10.22 21.93 10.23 31.71 0 11.45-5.76 20.28-12.75 29.81-1.31 1.79-2.61 3.5-3.87 5.16-7.61 10-9.28 12.89-8.18 18.05 2.23 10.37 18.86 41.24 46.19 68.51s57.31 42.85 67.72 45.07c5.38 1.15 8.33-.59 18.65-8.47 1.48-1.13 3-2.3 4.59-3.47 10.66-7.93 19.08-13.54 30.26-13.54h.06c9.73 0 18.06 4.22 31.86 11.18 18 9.08 59.11 33.59 77.14 51.78 8.77 8.84 13.66 14.48 16.05 20.81 3.6 9.53.21 17-2 22-.37.83-.78 1.74-1.21 2.75a176.49 176.49 0 01-15.29 28.58c-10.63 15.9-21.4 28.21-39.38 36.58A67.42 67.42 0 01391 480z"/></svg>Call (503) 555-0100</a>
</div>
```

**Code callout** (regular / warn):
```html
<div class="ea-callout">
  <div class="ea-callout-title"><svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M248 64C146.39 64 64 146.39 64 248s82.39 184 184 184 184-82.39 184-184S349.61 64 248 64z" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="32"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M220 220h32v116"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-miterlimit="10" stroke-width="32" d="M208 340h88"/><path d="M248 130a26 26 0 1026 26 26 26 0 00-26-26z"/></svg>Oregon Amendment &middot; OESC Table 1-E, 680.42(B)</div>
  <p>Body...</p>
</div>
<div class="ea-callout warn">
  <div class="ea-callout-title"><svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M85.57 446.25h340.86a32 32 0 0028.17-47.17L284.18 82.58c-12.09-22.44-44.27-22.44-56.36 0L57.4 399.08a32 32 0 0028.17 47.17z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path d="M250.26 195.39l5.74 122 5.73-121.95a5.74 5.74 0 00-5.79-6h0a5.74 5.74 0 00-5.68 5.95z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><path d="M256 397.25a20 20 0 1120-20 20 20 0 01-20 20z"/></svg>Title</div>
  <p>Body...</p>
</div>
```

**Comparison cards**:
```html
<div class="ea-compare">
  <div class="ea-card"><span class="ea-card-tag">Tag</span><h4>Title</h4><p>Body</p><div class="ea-card-spec"><strong>Spec:</strong> value</div></div>
  <div class="ea-card"><span class="ea-card-tag heavy">Tag</span><h4>Title</h4><p>Body</p><div class="ea-card-spec"><strong>Spec:</strong> value</div></div>
</div>
```

**Image** (real job photo; diagrams may be generated, see SKILL.md stage 7):
```html
<figure><img src="IMAGE_URL" alt="8 to 16 words describing what is visible" width="1200" height="675" loading="lazy"><figcaption>Caption. No location tags on residential work.</figcaption></figure>
```
Never ship a placeholder `src`. If the image is not uploaded yet, omit the figure and tell the user where it goes.

**Sources** (before FAQ):
```html
<div class="ea-sources"><strong>Sources</strong><ol>
  <li><a href="URL">Oregon BCD, 2023 OESC Table 1-E (amended Jan 1, 2026)</a></li>
</ol></div>
```

**FAQ** (5-7, first two open):
```html
<div class="ea-faq">
  <details open><summary>Question?</summary><div class="ea-faq-answer"><p>Answer.</p></div></details>
  <details open><summary>Question?</summary><div class="ea-faq-answer"><p>Answer.</p></div></details>
  <details><summary>Question?</summary><div class="ea-faq-answer"><p>Answer.</p></div></details>
</div>
```

**Final CTA** (last element, then close `.ea-post`):
```html
<div class="ea-final-cta">
  <h2>Headline</h2>
  <p>Licensed in Oregon (CCB# 000000) and Washington (EXAMPLE000XX). [ownership differentiators]. [N]+ reviews. Same-week scheduling for most projects.</p>
  <div class="ea-final-cta-btns">
    <a href="tel:5035550100" class="ea-btn"><svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M391 480c-19.52 0-46.94-7.06-88-30-49.93-28-88.55-53.85-138.21-103.38C116.91 298.77 93.61 267.79 61 208.45c-36.84-67-30.56-102.12-23.54-117.13C45.82 73.38 58.16 62.65 74.11 52a176.3 176.3 0 0128.64-15.2c1-.43 1.93-.84 2.76-1.21 4.95-2.23 12.45-5.6 21.95-2 6.34 2.38 12 7.25 20.86 16 18.17 17.92 43 57.83 52.16 77.43 6.15 13.21 10.22 21.93 10.23 31.71 0 11.45-5.76 20.28-12.75 29.81-1.31 1.79-2.61 3.5-3.87 5.16-7.61 10-9.28 12.89-8.18 18.05 2.23 10.37 18.86 41.24 46.19 68.51s57.31 42.85 67.72 45.07c5.38 1.15 8.33-.59 18.65-8.47 1.48-1.13 3-2.3 4.59-3.47 10.66-7.93 19.08-13.54 30.26-13.54h.06c9.73 0 18.06 4.22 31.86 11.18 18 9.08 59.11 33.59 77.14 51.78 8.77 8.84 13.66 14.48 16.05 20.81 3.6 9.53.21 17-2 22-.37.83-.78 1.74-1.21 2.75a176.49 176.49 0 01-15.29 28.58c-10.63 15.9-21.4 28.21-39.38 36.58A67.42 67.42 0 01391 480z"/></svg>Call (503) 555-0100</a>
    <a href="/servicearea/" class="ea-btn-secondary"><svg class="ea-ico" viewBox="0 0 512 512" aria-hidden="true"><path d="M256 48c-79.5 0-144 61.39-144 137 0 87 96 224.87 131.25 272.49a15.77 15.77 0 0025.5 0C304 409.89 400 272.07 400 185c0-75.61-64.5-137-144-137z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/><circle cx="256" cy="192" r="48" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32"/></svg>View Service Area</a>
  </div>
</div>
</div> <!-- /.ea-post -->
```

## Schema template (`[slug]-schema.txt`)

File starts with `<script` and ends with `</script>`. Nothing else, ever. Straight quotes, no em dashes, FAQ text identical to the visible page.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "[WP title]",
  "description": "[meta description]",
  "image": ["[16x9 URL]", "[4x3 URL]", "[1x1 URL]"],
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD, matches Last updated line]",
  "inLanguage": "en-US",
  "author": { "@type": "Organization", "name": "Example Electric", "url": "https://client.example" },
  "publisher": { "@type": "Organization", "@id": "https://client.example/#organization", "name": "Example Electric", "url": "https://client.example" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://client.example/blog/[slug]/" },
  "about": {
    "@type": "Service",
    "name": "[Service]",
    "provider": {
      "@type": "Electrician",
      "name": "Example Electric",
      "telephone": "+15035550100",
      "url": "https://client.example",
      "address": { "@type": "PostalAddress", "streetAddress": "[street address]", "addressLocality": "[city]", "addressRegion": "OR", "postalCode": "[zip]", "addressCountry": "US" },
      "areaServed": ["[match the post jurisdiction]"],
      "hasCredential": ["Oregon CCB# 000000", "Washington EXAMPLE000XX"]
    },
    "priceRange": "[only if the post states a verified range]"
  },
  "mainEntity": { "@type": "FAQPage", "mainEntity": [
    { "@type": "Question", "name": "[Q]", "acceptedAnswer": { "@type": "Answer", "text": "[plain text A]" } }
  ] }
}
</script>
```

Omit `image` if no image URL exists yet (an empty or placeholder URL is worse than none). Once an author page exists, swap `author` for `{ "@id": "https://client.example/about/[owner]/#person" }`.