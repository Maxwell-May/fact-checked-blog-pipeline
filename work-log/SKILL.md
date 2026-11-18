---
name: example-electric-work-log
description: Maintains the Example Electric work log and monthly performance reports. Auto-triggers MID-SESSION on completion signals ("done", "shipped", "deployed") AND at session end via Stop hook. Verifies with user before logging. Use for Example Electric SEO retainer project only.
compatibility: Read, Write, Edit, Bash, WebFetch, Agent
---

# Example Electric Work Log Skill

You maintain two living documents for the Example Electric SEO retainer:

1. **Master work log**: `~/clients/example-electric/outputs/example-electric-work-log.pdf` (source HTML at `example-electric-work-log-source.html` in same folder)
2. **Monthly reports**: `~/clients/example-electric/outputs/monthly-reports/<month>-<year>-report.html`

---

## TRIGGER BEHAVIOR: MID-SESSION (NEW)

In addition to session-end logging, this skill auto-triggers during the session when work appears complete.

### Auto-Trigger Signals

Detect these completion signals from the user OR from conversation flow:

**Explicit signals (from user):**
- "done", "done done", "shipped", "deployed", "published", "live", "wrapped", "finished"
- "okay that's done", "alright moved on", "next"
- Confirmation that a deploy worked: "looks good now", "it's live", "rendered correctly"
- Screenshots showing live deployment

**Implicit signals (from conversation flow):**
- User shifts to a clearly different task or topic
- User asks "what's next?" or similar
- Multiple confirmations on a task arrive, then a new topic starts
- A multi-step deploy plan reaches its final step + user confirms

### When a Signal Fires: Verification Flow

**Critical:** Always verify with the user before logging. Format:

> "Want me to log to the work log: **[short description of what shipped]**?"

If user confirms → log it immediately (don't wait for session end).
If user says no → skip silently.
If unclear → ask one short clarification: "Is the [X] piece fully shipped, or still pending some piece?"

### What to Log (mid-session entries)

Same structure as session-end logging:
1. Add to Key Wins section (concise, ~50-100 words)
2. Add to Work Completed table row with today's date
3. If content was published, add to Content Published table
4. If something moved from Pending → Done, update Carried Forward table
5. Always use today's actual date (check system context)

### What NOT to Log Mid-Session

- Planning / research / exploration without a deliverable
- Drafts that haven't been deployed
- Partial completions ("HTML built but not pasted to WP yet" → wait until user confirms it's live)
- Pure conversation / Q&A without an artifact

### Smart Detection Rules

- If user says "done with X" + clearly moves to Y, log X automatically (but still ask "want me to log [X]?" first)
- If multiple small wins accumulate in a session (review reply, GBP draft, image staged), batch them into one logging pass when triggered, not one entry per
- Don't ask to log every micro-action: wait for a real milestone

---

## TRIGGER BEHAVIOR: SESSION END (existing)

This skill also fires automatically at session end via Stop hook. When it runs:

1. **Review the conversation**: scan for any completed tasks NOT already logged mid-session.
2. **Update the master work log HTML source**: add any new completed items to the appropriate section.
3. **Update the monthly report** for the current month: add any new completed items.
4. **Regenerate the work log PDF**: run: `open -a "Google Chrome" --args --headless --disable-gpu --print-to-pdf="~/clients/example-electric/outputs/example-electric-work-log.pdf" file://~/clients/example-electric/outputs/example-electric-work-log-source.html` (only if significant changes were made)

If nothing meaningful was completed in the session, skip the update and say so.

---

## MASTER WORK LOG: WHAT TO TRACK

When something is COMPLETED, add it with:
- Date (today)
- Category (Technical / Content / GBP / Schema / Citations / On-Page / Social)
- What was done (1-2 sentences, specific)
- Impact if known (keyword movement, impressions, etc.)

When something CHANGES STATUS, update the relevant section table.

---

## MONTHLY REPORT: STRUCTURE

Generate or update `~/clients/example-electric/outputs/monthly-reports/<month>-<year>-report.html` using this HTML template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Example Electric: [Month Year] SEO Report</title>
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 32px; color: #1a1a2e; }
  h1 { background: #1a1a2e; color: white; padding: 18px 24px; border-radius: 8px; font-size: 1.4em; }
  h2 { background: #2d3561; color: white; padding: 10px 16px; border-radius: 6px; font-size: 1.1em; margin-top: 32px; }
  h3 { color: #2d3561; border-bottom: 2px solid #e8eaf6; padding-bottom: 4px; }
  table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 0.9em; }
  th { background: #2d3561; color: white; padding: 8px 12px; text-align: left; }
  td { padding: 8px 12px; border-bottom: 1px solid #e8eaf6; vertical-align: top; }
  tr:nth-child(even) { background: #f8f9ff; }
  .badge-done { background: #2e7d32; color: white; padding: 2px 10px; border-radius: 4px; font-size: 0.82em; font-weight: bold; }
  .badge-pending { background: #e65100; color: white; padding: 2px 10px; border-radius: 4px; font-size: 0.82em; font-weight: bold; }
  .badge-progress { background: #1565c0; color: white; padding: 2px 10px; border-radius: 4px; font-size: 0.82em; font-weight: bold; }
  .metric-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 16px 0; }
  .metric-box { background: #f8f9ff; border: 1px solid #e8eaf6; border-radius: 8px; padding: 16px; text-align: center; }
  .metric-box .value { font-size: 2em; font-weight: bold; color: #2d3561; }
  .metric-box .label { font-size: 0.85em; color: #666; margin-top: 4px; }
  .metric-box .change { font-size: 0.9em; color: #2e7d32; font-weight: bold; }
  .win { background: #e8f5e9; border-left: 4px solid #2e7d32; padding: 10px 14px; margin: 8px 0; border-radius: 0 6px 6px 0; }
  .note { background: #fff8e1; border-left: 4px solid #f9a825; padding: 10px 14px; margin: 8px 0; border-radius: 0 6px 6px 0; font-size: 0.9em; }
  footer { margin-top: 48px; font-size: 0.8em; color: #999; text-align: center; border-top: 1px solid #e8eaf6; padding-top: 16px; }
</style>
</head>
<body>

<h1>⚡ Example Electric: [Month Year] SEO Retainer Report</h1>
<p style="color:#666; font-size:0.9em;">Retainer: [price]/mo · Prepared by: Max · Date: [Report Date]<br>
CCB# 000000 · client.example · (503) 555-0100</p>

<!-- KEY METRICS SECTION -->
<h2>📊 Key Metrics</h2>
<div class="metric-grid">
  <div class="metric-box">
    <div class="value">[X]</div>
    <div class="label">Weekly Organic Visits (Ahrefs)</div>
    <div class="change">▲ from [X] last month</div>
  </div>
  <div class="metric-box">
    <div class="value">[X]</div>
    <div class="label">GSC Clicks (month)</div>
    <div class="change">▲ from [X] last month</div>
  </div>
  <div class="metric-box">
    <div class="value">[X]</div>
    <div class="label">GSC Impressions (month)</div>
    <div class="change">▲ from [X] last month</div>
  </div>
  <div class="metric-box">
    <div class="value">[X]</div>
    <div class="label">Ranking Keywords (GSC)</div>
    <div class="change">was [X]</div>
  </div>
  <div class="metric-box">
    <div class="value">[X]</div>
    <div class="label">Avg Position (GSC)</div>
    <div class="change">was [X]</div>
  </div>
  <div class="metric-box">
    <div class="value">[X]</div>
    <div class="label">Ahrefs Health Score</div>
    <div class="change">was [X]</div>
  </div>
</div>

<!-- KEY WINS -->
<h2>🏆 Key Wins This Month</h2>
<!-- Add .win divs here -->

<!-- WORK COMPLETED LOG -->
<h2>✅ Work Completed</h2>
<table>
  <tr><th>Date</th><th>Category</th><th>Task</th><th>Impact</th></tr>
  <!-- Add rows here -->
</table>

<!-- KEYWORD MOVEMENTS -->
<h2>📈 Keyword Movements</h2>
<table>
  <tr><th>Keyword</th><th>Vol</th><th>Start of Month</th><th>End of Month</th><th>Change</th><th>Page</th></tr>
  <!-- Add rows here -->
</table>

<!-- CONTENT PUBLISHED -->
<h2>📝 Content Published</h2>
<table>
  <tr><th>Title</th><th>URL</th><th>Published</th><th>Type</th><th>Status</th></tr>
  <!-- Add rows here -->
</table>

<!-- PENDING / NEXT MONTH -->
<h2>⏳ Carried Forward to Next Month</h2>
<table>
  <tr><th>Item</th><th>Priority</th><th>Notes</th></tr>
  <!-- Add rows here -->
</table>

<footer>
  Example Electric SEO Retainer · [price]/mo · Generated [Date] · Ask Claude to regenerate at any time.
</footer>
</body>
</html>
```

---

## RULES

- **Never fabricate data.** Only log what actually happened in the session or is verifiable from Ahrefs/GSC MCP tools.
- **Be specific.** "Fixed [city] page title/meta: was [x]% CTR, [n] impressions" beats "improved [city] page."
- **Don't pad.** If two things were done, log two things. Don't invent sub-tasks.
- **Date accuracy.** Use today's actual date (available in system context).
- **Monthly reports are cumulative.** Each new session adds to the month's report; never overwrites existing entries.

---

## CURRENT MONTHLY REPORT STATUS

- April 2026 report: `~/clients/example-electric/outputs/monthly-reports/april-2026-report.html`

At end of April, flag to user: "April is closing: want me to finalize the monthly report and start May?"
