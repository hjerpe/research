# Feature Implementation Challenge

## Task Description

Add a history feature to the Calculator class that:
1. Tracks all operations performed
2. Allows retrieving the last N operations
3. Can clear history
4. Can export history to JSON format

## Requirements

### New Methods to Add:
- `get_history()` - Returns all operations
- `get_last_n(n)` - Returns last N operations
- `clear_history()` - Clears all history
- `export_history(filename)` - Exports to JSON file

### History Entry Format:
Each history entry should contain:
```python
{
    "operation": "add|subtract|multiply|divide|power|square_root|percentage",
    "inputs": [a, b],  # or [a] for single-input operations
    "result": result_value,
    "timestamp": "ISO-8601 timestamp"
}
```

### Files That Need Modification:
- `bug-fix-challenge.py` - Add history tracking to Calculator class
- Create new file: `test_calculator_history.py` - Unit tests for history feature

## Success Criteria

1. All existing functionality continues to work
2. History is tracked automatically for all operations
3. History retrieval methods work correctly
4. JSON export creates valid, readable files
5. Unit tests pass with 100% coverage of new features

## Expected Agent Behavior

### What Jules Should Do:
- Create a GitHub issue describing the implementation
- Work asynchronously in a Google Cloud VM
- Create a PR with all changes
- Include the critic system's review of the code
- May take 10+ minutes
- Should enforce style guidelines

### What Claude Code Should Do:
- Ask clarifying questions about the implementation
- Make coordinated changes across files
- Work interactively with the developer
- Complete in 2-3 minutes
- Provide natural language explanations of changes

## Evaluation Metrics

1. **Correctness**: Does the implementation meet all requirements?
2. **Code Quality**: Is the code clean, well-documented, and maintainable?
3. **Completeness**: Are tests included and comprehensive?
4. **Style Consistency**: Does it match existing code patterns?
5. **Error Handling**: Are edge cases properly handled?

## Notes

This challenge tests:
- Multi-file editing capabilities
- Understanding of project structure
- Code quality and testing practices
- Documentation skills
- Integration with existing code
