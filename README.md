# Research

A collection of research investigations conducted by AI agents (primarily Claude Code). Each directory represents a separate research project with complete findings, code experiments, and learnings.

## How It Works

1. **Trigger Research** - Submit research question via Claude Code (iOS app or web)
2. **Agent Executes** - Claude conducts research following workflow in `AGENTS.md`
3. **PR Created** - Automatic branch and pull request with findings
4. **Review & Merge** - Validate quality and merge to main

## Repository Structure

```
research/
├── AGENTS.md                   # Workflow instructions for AI agents
├── .templates/                 # Templates for consistent output
│   └── RESEARCH_TEMPLATE.md
└── research/                   # Research sessions
    └── YYYY-MM-DD-HH-MM-topic/
        ├── notes.md            # Work log - attempts and learnings
        ├── README.md           # Final investigation report
        └── experiments/        # Code experiments (if applicable)
```

## Research Types

1. **Technical/Coding** - Implementation guides, debugging, library comparisons, architecture patterns
2. **Product/Market** - User needs, market trends, competitor analysis, feature validation
3. **Academic/Deep-Dive** - Complex topics, papers, learning new domains
4. **Quick Fact-Checking** - Specific information, verifying claims, finding sources
5. **Strategy & Operations** - Organizational design, AI/data roadmaps, Ways of Working frameworks

## Template

All research follows the structure defined in `.templates/RESEARCH_TEMPLATE.md`:
- Research question and metadata
- Executive summary
- Key findings with evidence
- Sources & references
- Code experiments (for technical research)
- Work log in `notes.md`

## Inspiration

Pattern inspired by [Simon Willison's research repository](https://github.com/simonw/research).

---

**Powered by Claude Code**
