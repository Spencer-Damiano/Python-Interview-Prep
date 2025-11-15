# Problem Template for Solutions

Use this format for all problem files. Problems should be self-contained with NO hints or solutions in the initial presentation.

## File Naming Convention
Use descriptive kebab-case: `problem-name.py`

Examples:
- `group-by-grade.py`
- `count-character-frequency.py`
- `find-first-duplicate.py`

## Problem File Structure
```python
"""
Problem: [Clear, Descriptive Title]
Difficulty: Easy
Category: Hashmaps/Dictionaries
Date: YYYY-MM-DD

[Clear problem description explaining what needs to be done]

[Concrete example with input and expected output]

Example:
Input: [show example input]
Output: [show expected output]

[Optional: Additional examples if needed for clarity]

Constraints:
- [List any constraints on input size]
- [List any assumptions about data types]
- [List any edge cases to consider]
"""

def function_name(parameter):
    """
    [Brief description of what the function should do]
    
    Args:
        parameter: [description of parameter type and meaning]
    
    Returns:
        [description of return type and meaning]
    """
    # Your code here
    pass


# Test cases (don't look at these until you've attempted the problem!)
if __name__ == "__main__":
    # Test 1: [Description of what this tests]
    test_input_1 = [...]
    
    # Test 2: [Description of what this tests]
    test_input_2 = [...]
    
    # Test 3: [Description of edge case]
    test_input_3 = [...]
    
    print("Test 1:", function_name(test_input_1))
    # Expected: [expected output]
    
    print("Test 2:", function_name(test_input_2))
    # Expected: [expected output]
    
    print("Test 3:", function_name(test_input_3))
    # Expected: [expected output]
```

## Requirements for Problems

**Problem Description Must Include:**
- Clear statement of the task
- At least one concrete example with input/output
- Constraints and assumptions
- Edge cases to consider

**What NOT to Include:**
- Hints about the approach
- Solution strategies
- Time/space complexity expectations (I'll figure those out)
- "Think about using X data structure" suggestions

**Test Cases Should:**
- Cover the basic/happy path
- Include at least one edge case
- Show expected output clearly
- Be hidden at the bottom so I don't see them immediately

**Difficulty Calibration:**
- Easy: Straightforward hashmap operations (lookup, counting, grouping)
- Should be solvable in 20-30 minutes
- Focus on fundamentals, not tricks

## Weekly README Template

Each week folder should have a README.md:
```markdown
# Week [N] - [Date Range]

## Focus
[What category/concept this week focused on]

## Problems Solved
- `filename.py` - [One-line description]
- `filename.py` - [One-line description]

## What I Learned
- [Key takeaway 1]
- [Key takeaway 2]

## Challenges
[What was hard this week]

## Energy Level
[Notes about capacity this week]

## Next Week Goals
[What to focus on next]
```

## Example Problem (Reference)

See `week-01-nov-11/group-by-grade.py` for a properly formatted problem following this template.