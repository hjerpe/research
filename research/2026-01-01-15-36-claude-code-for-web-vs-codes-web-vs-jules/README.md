# Claude Code for Web vs Codes Web vs Jules (Google)

**Date:** 2026-01-01 15:36  
**Type:** product

## Research Question

Conduct a research investigation comparing the pros and cons of "Claude Code for Web", "Codes Web", and "https://jules.google/".

## Executive Summary

Claude Code on the web and Jules are both autonomous coding agents that run tasks in cloud environments and integrate with GitHub, but they differ in access models, workflow details, and operational limits. Claude Code on the web is a research preview for specific paid tiers and operates from the Claude app with a dedicated Anthropic-managed VM, configurable network access, and GitHub-only repositories. Jules positions itself as an experimental agent with explicit task/concurrency limits by plan, GitHub integration, and a workflow centered on planning, diffs, and PRs, powered by Gemini models.

“Codes Web” appears to be either a non-public or unindexed product: the domain `codes.web` did not resolve in DNS from this environment and no search results referenced a product by that name. As a result, the comparison below highlights the verified pros/cons of Claude Code on the web and Jules, and explicitly calls out the lack of public sources for Codes Web.

## Key Findings

- **Claude Code on the web is a research preview for paid Claude tiers and runs tasks in an Anthropic-managed cloud VM with GitHub-only repos.** The docs state it is available to Pro, Max, Team premium seat, and Enterprise premium seat users, requires GitHub app installation, and limits cloud sessions to GitHub-hosted code. It also supports moving tasks from web to local CLI. [Source](https://code.claude.com/docs/en/claude-code-on-the-web)
- **Claude Code on the web emphasizes secure, configurable network access and a prebuilt universal image.** It runs in isolated VMs, uses network proxies, and allows limited/disabled network access, with a default allowlist of domains and a universal image that includes common languages and tooling. [Source](https://code.claude.com/docs/en/claude-code-on-the-web)
- **Jules advertises an autonomous workflow that clones GitHub repos to a cloud VM, runs tests, and creates PRs.** The product page describes GitHub integration, cloud VM execution, test running, and a plan/diff/PR workflow. [Source](https://jules.google/)
- **Jules documentation labels the tool as experimental and explains onboarding steps and GitHub integration.** The getting-started doc notes Jules is an experimental coding agent, requires Google login and GitHub connection, and supports task execution within connected repos. [Source](https://jules.google/docs)
- **No public, verifiable sources for “Codes Web” were found.** DNS resolution for `codes.web` failed and DuckDuckGo searches for "Codes Web" returned no relevant results. This is a material gap that prevents a definitive comparison for that product. (See `notes.md` for details.)

## Comparison: Pros and Cons (Evidence-backed)

### Claude Code on the web (Anthropic)
**Pros**
- Clear eligibility and access model (research preview for paid tiers) with explicit onboarding steps. [Source](https://code.claude.com/docs/en/claude-code-on-the-web)
- Cloud execution with configurable network access and strong isolation guarantees. [Source](https://code.claude.com/docs/en/claude-code-on-the-web)
- Supports moving tasks from web to local terminal to continue work. [Source](https://code.claude.com/docs/en/claude-code-on-the-web)

**Cons**
- Cloud sessions are limited to GitHub-hosted repositories; GitLab and other hosts are excluded. [Source](https://code.claude.com/docs/en/claude-code-on-the-web)
- Usage is gated to paid tiers and shares account-wide rate limits. [Source](https://code.claude.com/docs/en/claude-code-on-the-web)

### Jules (Google)
**Pros**
- End-to-end agent workflow: fetch repo, plan, implement changes, run tests, and propose PRs. [Source](https://jules.google/)
- Explicit plan tiers with task and concurrency limits to match different workflow scales. [Source](https://jules.google/)
- Experimental status and onboarding steps clearly documented (Google login + GitHub connection). [Source](https://jules.google/docs)

**Cons**
- Marketed as experimental; production readiness and stability may be evolving. [Source](https://jules.google/docs)
- Plan details list task/concurrency limits but no pricing is stated on the public page. [Source](https://jules.google/)

### Codes Web
**Pros**
- No verified public sources available.

**Cons**
- `codes.web` did not resolve via DNS in this environment, and no authoritative sources were found in search results, preventing feature or pricing validation. (See `notes.md`.)

## Sources & References

1. [Claude Code on the web - Claude Code Docs](https://code.claude.com/docs/en/claude-code-on-the-web) - Eligibility, workflow, cloud environment, security, and limitations for Claude Code on the web.
2. [Jules - An Autonomous Coding Agent](https://jules.google/) - Product overview, workflow steps, GitHub integration, cloud VM execution, and plan/task limits.
3. [Jules Documentation - Getting started](https://jules.google/docs) - Experimental status, onboarding flow, and GitHub connection requirements.

## Next Steps / Open Questions

- [ ] Confirm whether “Codes Web” is a public product, a private beta, or a mislabeling (e.g., alternate branding) and obtain an official source.
- [ ] Capture pricing details for Jules and Claude Code on the web if available on official plan pages.
- [ ] Validate any enterprise compliance or data-handling policies for both platforms to inform governance decisions.

---

*Research conducted by Claude Code | [View notes.md for work log](notes.md)*
