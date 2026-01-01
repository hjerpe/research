# Research Workflow Instructions

**For Claude Code agents conducting research in this repository.**

When you receive a research prompt, follow this complete workflow. All requirements are specified here - the prompt only needs to provide the research question and type.

---

## Standard Prompt Format

Research prompts will look like this:

```
Research Topic: [technical/product/academic/quick-fact/strategy]

"[Research question]"

Follow AGENTS.md workflow.
```

That's it! Everything else is defined below.

---

## Complete Workflow

### Step 1: Create Research Directory
- Create folder: `research/YYYY-MM-DD-HH-MM-[topic-slug]/`
  - Use current date/time
  - Create URL-friendly slug from research topic
  - Example: `research/2026-01-15-14-30-asyncio-vs-threading/`

### Step 2: Start Work Log
- Create `notes.md` in the research directory
- Document your research process as you work:
  - Initial approach and hypotheses
  - Sources and tools explored
  - What worked, what didn't, and why
  - Dead ends and pivots
  - Breakthrough moments
  - Key learnings during the process

### Step 3: Conduct Research
- **Use web search** to find current, authoritative sources
- Cross-check facts across multiple sources
- Prioritize recent, credible sources
- Gather at least 3-5 diverse sources
- For technical research: Write and test code experiments
- For product research: Compare alternatives, note pricing
- For academic research: Prioritize peer-reviewed sources
- Update `notes.md` as you explore

### Step 4: Create Experiments (Technical Research Only)
- Create `experiments/` subdirectory
- Write working code examples that validate findings
- Test all code - it MUST run successfully
- Include setup instructions and requirements
- Document results and performance data

### Step 5: Write Final Report
- Create `README.md` following `.templates/RESEARCH_TEMPLATE.md`
- Include all required sections:
  - Research question and metadata (date, type)
  - Executive summary (1-3 paragraphs for busy readers)
  - Key findings (bulleted, evidence-backed)
  - Sources & references (with URLs and descriptions)
  - Code experiments section (if technical research)
  - Next steps or open questions (optional)

### Step 6: Create Branch & Commit
- Create branch: `research/[topic-slug]`
  - Example: `research/asyncio-vs-threading`
- Commit files with clear, descriptive messages
- Include:
  - ✅ `notes.md` (work log)
  - ✅ `README.md` (final report)
  - ✅ `experiments/` directory with code (if applicable)
  - ✅ Small relevant artifacts (<2MB)
- Exclude:
  - ❌ Full copies of external code/repos
  - ❌ Large binary files (>2MB)
  - ❌ Dependencies or node_modules

### Step 7: Create Pull Request
- Create PR with summary of key findings in description
- Highlight most important insights
- Reference any related issues or previous research
- PR will be reviewed before merging

---

## Quality Standards

### For All Research Types:
- ✅ Cite all sources with URLs
- ✅ Use current, authoritative sources - verify information is up-to-date
- ✅ Cross-check facts across multiple sources when possible
- ✅ Include at least 3 diverse sources
- ✅ Provide clear, actionable insights
- ✅ Write executive summary for busy readers
- ✅ Use web search to find information

### For Technical/Coding Research:
- ✅ All code examples MUST run successfully
- ✅ Create working experiments in `experiments/` directory
- ✅ Include setup/installation instructions
- ✅ Test on latest stable versions
- ✅ Document any system requirements
- ✅ Include benchmarks or performance data when relevant

### For Product/Market Research:
- ✅ Compare multiple alternatives (at least 2-3)
- ✅ Include pricing information where applicable
- ✅ Note dates of information (market data changes frequently)
- ✅ Summarize pros/cons clearly
- ✅ Include real-world examples or case studies

### For Academic/Deep-Dive Research:
- ✅ Prioritize peer-reviewed sources and academic papers
- ✅ Define key technical terms
- ✅ Explain complex concepts accessibly
- ✅ Note conflicting viewpoints or ongoing debates
- ✅ Include historical context when relevant

### For Quick Fact-Checking:
- ✅ Focus on speed without sacrificing accuracy
- ✅ Use authoritative primary sources
- ✅ Include publication dates (recency matters)
- ✅ Note any conflicting information found
- ✅ Keep it concise - executive summary can be 1 paragraph

### For Strategy/Operations Research:
- ✅ Include frameworks and mental models
- ✅ Provide case studies or real-world examples
- ✅ Summarize different schools of thought
- ✅ Focus on actionable insights
- ✅ Create diagrams if helpful (mermaid or ASCII)

---

## Research Type Guidelines

Tailor your approach based on research type specified in the prompt:

**Technical/Coding**
- Focus on working code, benchmarks, comparisons
- Must include tested code experiments
- Compare multiple approaches/libraries when applicable

**Product/Market**
- Focus on trends, competitors, user needs
- Include market data with dates
- Compare alternatives with pros/cons

**Academic**
- Focus on depth, accuracy, authoritative sources
- Use peer-reviewed papers when available
- Explain concepts for general technical audience

**Quick Fact**
- Focus on speed and accuracy
- Use authoritative primary sources
- Be concise but thorough

**Strategy/Ops**
- Focus on frameworks, case studies, actionable insights
- Include different perspectives
- Provide implementation guidance

---

## Template Reference

Always structure `README.md` following `.templates/RESEARCH_TEMPLATE.md`.

Required sections:
1. Title and metadata (date, type)
2. Research question
3. Executive summary
4. Key findings
5. Sources & references
6. Code experiments (if technical)
7. Next steps (optional)

---

## Important Reminders

- **Use web search actively** - Don't rely solely on training data
- **Test all code** - Code that doesn't run is not acceptable
- **Cite sources with URLs** - Every claim needs a source
- **Update notes.md throughout** - Not just at the end
- **Quality over speed** - Thorough research is more valuable
- **Cross-check facts** - Verify information across sources

---

**When in doubt, prioritize thoroughness and accuracy over speed.**
