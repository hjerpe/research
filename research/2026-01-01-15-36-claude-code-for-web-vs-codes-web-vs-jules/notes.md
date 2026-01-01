# Work Log

## Initial approach and hypotheses
- Gather primary sources from each product's official site and docs.
- Compare on access model, supported workflows, integrations, pricing/availability, and limitations.

## Sources and tools explored
- DuckDuckGo HTML search via Playwright (Firefox) to discover official docs and announcements.
- Official product/documentation pages for Claude Code on the web and Jules.
- Attempted to resolve and access codes.web directly.

## Progress updates
- Located Claude Code on the web documentation and extracted eligibility, workflow, and limitations.
- Located Jules product page and documentation to capture workflow, integration, and plan limits.
- Attempted to access Codes Web (codes.web) and search for references; no DNS resolution or results found.

## Dead ends and pivots
- Direct HTTPS requests from the shell returned 403 CONNECT tunnel errors.
- Chromium-based Playwright crashed; switched to Firefox Playwright, which worked.
- "Codes Web" did not resolve via DNS and produced no search results, so the comparison is limited to noting lack of publicly discoverable information.

## Breakthrough moments
- Using DuckDuckGo's HTML results with Firefox Playwright provided reliable search results and access to official sources.

## Key learnings during the process
- Claude Code on the web is a research preview in Claude, available to paid tiers, and runs tasks in an Anthropic-managed VM with GitHub-only repos and configurable network access.
- Jules is an experimental autonomous coding agent with GitHub integration, cloud VM execution, and explicit task/concurrency limits by plan.
- No publicly discoverable sources for "Codes Web" were found; domain does not resolve in DNS from this environment.

## Source access notes
- Claude Code on the web documentation: https://code.claude.com/docs/en/claude-code-on-the-web
- Jules product page: https://jules.google/
- Jules documentation: https://jules.google/docs
