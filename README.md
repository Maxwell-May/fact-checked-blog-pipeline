# Fact-checked blog pipeline

This is the workflow behind the blog posts I produce for one of my SEO clients, a licensed electrical contractor in the Portland, Oregon area. It is a Claude Code skill: a set of instructions, four agent prompts and a few small scripts that Claude follows from topic to finished post.

A post about electrical code has to be right, and a language model will happily write a wrong one that sounds great. So nothing in a post gets written until it has been checked against its source.

## How it works

1. Two research agents gather the facts. Each fact goes into a table, the claim ledger, with its source link and the exact quote.
2. A third agent tries to break every row. It opens each source itself and gives the row a verdict: confirmed, corrected, estimate or dropped.
3. `check_ledger.py` reads the checked table and prints GATE OPEN or BLOCKED. A row with no verdict or no source blocks it. So does a table it cannot read.
4. The post is written only from the rows that passed.
5. `lint_post.py` checks the finished files against 40-plus rules. Every rule is a mistake that got through once.
6. A fourth agent reviews the post and answers SHIP or DO NOT SHIP.
7. I decide whether it goes live, and I paste it into WordPress myself.

The full design, with the failures that shaped it, is in [blog-pipeline/README-PIPELINE.md](blog-pipeline/README-PIPELINE.md).

## Where to look

| File | What it is |
|---|---|
| [blog-pipeline/SKILL.md](blog-pipeline/SKILL.md) | The step-by-step instructions Claude follows |
| [blog-pipeline/agents/claim-checker.md](blog-pipeline/agents/claim-checker.md) | The prompt for the agent that tries to break every fact |
| [blog-pipeline/scripts/check_ledger.py](blog-pipeline/scripts/check_ledger.py) | The gate before writing |
| [blog-pipeline/scripts/lint_post.py](blog-pipeline/scripts/lint_post.py) | The rules the finished post has to pass |
| [blog-pipeline/scripts/render_table1e.sh](blog-pipeline/scripts/render_table1e.sh) | The fix for the worst mistake it made, described below |
| [blog-pipeline/scripts/test_fixtures.sh](blog-pipeline/scripts/test_fixtures.sh) | Tests for the gate and the lint |
| [blog-pipeline/reference/company-and-rules.md](blog-pipeline/reference/company-and-rules.md) | What the client can and cannot claim |
| [work-log/SKILL.md](work-log/SKILL.md) | A second workflow that asks me before it files finished work in the client's work log and monthly report |

## The mistake that shaped it

A post said Oregon "adds this sentence" to a national rule. Oregon had added two words, "or deck". Oregon publishes its changes to the national electrical code as a PDF table and marks what it added with underlining. The agent had read the PDF as plain text, which drops the underlining. Now `render_table1e.sh` turns the page into an image and the agent reads the image. The claim checker makes its own image instead of trusting the researcher's quote.

## Who did what

Claude wrote the code. My part is deciding what the workflow has to guarantee, running it on real posts, and having Claude add a rule every time something wrong gets through or I fix a draft myself.

## What it is not

It is a skill that runs on my laptop when I start it. It is not a service: there is no logging, no monitoring and no deployment. The gate is a script plus an instruction to stop, so nothing physically prevents the writer from starting. The claim checker is a model too, so a second opinion lowers the odds of a wrong fact but does not remove them. That is why a person ships every post.

## Running the tests

```bash
bash blog-pipeline/scripts/test_fixtures.sh
```

This needs bash and Python 3. It runs 14 cases against the gate. Eight more cases test the lint against a real published post. That post is not included here, so those cases are skipped in this copy.

## What I changed for this public copy

The client's name, owner, address, phone numbers, license numbers, search-performance figures and retainer price are replaced with placeholders such as "Example Electric" and `client.example`. So are my account IDs and local paths. The test script has one added line saying the lint cases are skipped, and the long dashes in the work log file are now plain punctuation. Nothing else was changed.
