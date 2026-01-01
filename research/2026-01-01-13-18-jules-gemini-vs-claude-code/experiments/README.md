# Experiments Directory

This directory contains code experiments designed to evaluate Jules and Claude Code performance on practical software development tasks.

## Files

### 1. `bug-fix-challenge.py`
A simple Calculator class with intentional bugs:
- Division by zero not handled
- Negative number square root crashes

**Purpose:** Test bug detection and fixing capabilities

**To Run:**
```bash
python bug-fix-challenge.py
```

**To Test Bugs:**
Uncomment the commented lines in `main()` to trigger the bugs.

### 2. `feature-implementation-task.md`
Specification for adding a history tracking feature to the Calculator class.

**Purpose:** Test multi-file feature implementation capabilities

**Task Complexity:**
- Multi-file changes required
- JSON export functionality
- Unit test creation
- Integration with existing code

### 3. `EXPERIMENT_RESULTS.md`
Comprehensive analysis of expected performance for both agents based on:
- SWE-bench Verified benchmark data
- Documented workflows
- User reviews and comparisons
- Official capabilities

## How to Use These Experiments

### Testing with Jules:
1. Create a GitHub repository with these files
2. Create an issue describing the task (use `feature-implementation-task.md`)
3. Assign the issue to Jules at https://jules.google/
4. Wait for Jules to complete and create a PR
5. Review the PR and compare to expectations in `EXPERIMENT_RESULTS.md`

### Testing with Claude Code:
1. Open these files in your local environment
2. Start Claude Code in the terminal
3. Describe the task from `feature-implementation-task.md`
4. Work interactively with Claude Code
5. Compare results to expectations in `EXPERIMENT_RESULTS.md`

## Expected Outcomes

Based on SWE-bench Verified scores:
- **Claude Code**: ~85-92% success rate on these tasks
- **Jules**: ~75-85% success rate on these tasks

See `EXPERIMENT_RESULTS.md` for detailed analysis.

## Requirements

```bash
python >= 3.8
```

No external dependencies required for the bug-fix challenge.
Feature implementation task will require `json` module (Python standard library).
