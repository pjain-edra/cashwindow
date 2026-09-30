# CashWindow

A zero-dependency Python prototype that uses live SerpApi Google results to assemble a source-linked opportunity screening ledger. It flags possible entry costs, human attendance, AI restrictions, competitive prizes and dates outside a chosen cash window. It never converts a search result or prize pool into earned revenue.

## Run

Python 3.10+; no paid software or packages required.

Set `SERPAPI_API_KEY` privately in the environment. Do not commit the key. Run `python cashwindow.py --query "India online hackathon AI allowed cash prize" --output evidence.json`.

Offline demonstration: `python cashwindow.py --fixture fixture.json --output demo-evidence.json`. Fixtures are synthetic and clearly marked; they are not live SerpApi results. Tests: `python -m unittest -v`.

## Current status

Offline prototype and restriction tests complete. Live SerpApi integration verified September 30, 2026 with three authenticated searches; sanitized results are in live-evidence.json. demo.html is a searchable snapshot of those results. CashWindow-Demo.mp4 is a 60-second captioned demonstration. Some broad-query results are irrelevant; search completion does not validate an opportunity. No live-query performance, cash outcomes, user adoption or completeness claims are made. No project has been submitted to the hackathon.

## Limits

Rules operate on snippets, not full source terms. Keyword flags are review prompts, not eligibility decisions. ISO dates in snippets may describe any event, including publication dates; they are not inferred payment deadlines. Sources require verification, and search results can be stale or incomplete. The tool does not automatically apply, send messages or handle payments.

## SerpApi India Hackathon entry draft

Track: Knowledge & Public Interest. New project created September 30, 2026. SerpApi is central to discovery: without its live search results the tool only accepts offline fixtures. AI tools: ChatGPT/Codex for research, code, tests and documentation; disclose principal AI production. Human applicant owns accounts and performs essential authorization only.

Completed: free SerpApi access, three live searches and public GitHub source. Next requirements: public demonstration video under three minutes, participant phone and years of professional experience, GitHub-authenticated submission, and acceptance of contest terms. Do not submit until these requirements are met.
