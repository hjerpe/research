# Research Workflow Instructions

When conducting research, follow this workflow:

## 1. Folder Organization
- Create new folder: `research/YYYY-MM-DD-HH-MM-[topic-slug]/`
- All research artifacts go in this folder

## 2. Required Files

### notes.md
- Track attempts, experiments, and learnings as you work
- Document what works, what doesn't, and why
- This is your work log - keep it updated throughout research
- Include:
  - Initial approach and hypotheses
  - Tools and sources explored
  - Dead ends and why they didn't work
  - Breakthrough moments and insights
  - Time spent on different aspects

### README.md
- Final investigation report (use template from `.templates/RESEARCH_TEMPLATE.md`)
- Clear, polished summary of findings
- Include all key insights and sources
- This is what readers will see first

## 3. What to Include in Commits
- ✅ notes.md and README.md files
- ✅ Original code you created (experiments, examples, benchmarks)
- ✅ Small artifacts relevant to research (<2MB)
- ✅ Clear, descriptive commit messages
- ❌ Do NOT include full copies of external code or repos
- ❌ Do NOT include large binary files (>2MB)
- ❌ Do NOT include dependencies or node_modules

## 4. Branch & PR Workflow
1. Create branch: `research/[topic-slug]`
2. Commit work incrementally with clear messages
3. Create PR with summary of key findings in description
4. Reference any related issues or previous research

## 5. Quality Standards

### For All Research:
- Cite all sources with URLs
- Use current, authoritative sources - verify information is up-to-date
- Cross-check facts across multiple sources when possible
- Include at least 3 diverse sources
- Provide clear, actionable insights
- Write executive summary for busy readers

### For Technical Research:
- All code examples MUST run successfully
- Include setup/installation instructions
- Test on latest stable versions
- Document any system requirements
- Create working experiments in `experiments/` directory

### For Product/Market Research:
- Include pricing where applicable
- Compare multiple alternatives
- Note dates of information (market data changes frequently)
- Summarize pros/cons clearly

### For Academic Research:
- Prioritize peer-reviewed sources
- Define key terms
- Explain complex concepts accessibly
- Note conflicting viewpoints if they exist

## 6. Research Types

Tailor your approach based on research type:

- **Technical/Coding**: Focus on working code, benchmarks, comparisons
- **Product/Market**: Focus on trends, competitors, user needs
- **Academic**: Focus on depth, accuracy, authoritative sources
- **Quick Fact**: Focus on speed and authoritative primary sources
- **Strategy/Ops**: Focus on frameworks, case studies, actionable insights

## 7. Template Reference

Always use the structure from `.templates/RESEARCH_TEMPLATE.md` for README.md.

Customize based on research type, but maintain core sections:
- Research question
- Executive summary (1-3 paragraphs)
- Key findings (bulleted, evidence-backed)
- Sources & references
- Code experiments (if technical)
- Next steps or open questions

---

**Remember:** Focus on quality over speed. Thorough research with clear citations is more valuable than quick, incomplete work.
