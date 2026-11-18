# Keyword and gap data (stage 1)

Ahrefs project for the site: `project_id <project-id>` (client.example). Load schemas first with `ToolSearch select:<Ahrefs prefix>gsc-keywords,gsc-pages,keywords-explorer-overview,keywords-explorer-matching-terms,serp-overview,site-explorer-organic-keywords,doc`; call `<prefix>doc` for any input schema you have not used before.

| Call | Use |
|---|---|
| `gsc-keywords` (project_id, date_from, date_to, `where` on position/impressions) | Non-brand queries with impressions and zero clicks at positions 4-20: the demand the site is already near |
| `gsc-pages` | Which existing URL absorbs a query cluster (cannibalization) |
| `keywords-explorer-overview` (country `us`, `select` volume,difficulty,cpc,parent_topic) | Volume and difficulty for candidate heads and variants |
| `keywords-explorer-matching-terms` / `keywords-explorer-search-suggestions` | Long-tail and question variants for H2s and FAQ |
| `serp-overview` (country `us`, keyword) | Who ranks now, what format wins, what to out-inform |
| `site-explorer-organic-keywords` (target client.example) | Current rankings for the cluster |

**If any call returns `Insufficient plan`** (the API add-on has lapsed), do not retry or guess. Fall back to the Search Console export:

```bash
python3 SKILL_DIR/scripts/gsc_gaps.py ~/Downloads/<latest gsc export dir> --existing-slugs <slug list>
```

It prints the data window, clusters ranked by opportunity, which existing post already covers each cluster, zero-click informational queries, and the CTR reality check. State in the delivery which source was used and its window.

**Questions for the researchers (6-10).** With Ahrefs: question variants from `matching-terms` / `search-suggestions`. With the export: the cluster's top queries plus the zero-click informational list, plus the obvious homeowner questions (what it costs, whether a permit is needed, when to call).

**Do not pitch title or meta rewrites for zero-click top-3 terms.** Non-brand CTR at positions 1-3 on this site is a fraction of a percent; those impressions are AI Mode fan-out, not people (see research-standards, AI-surface caveat).
