"""
Problem: Group Students by Grade Range
Difficulty: Easy
Category: Hashmaps/Dictionaries
Completed: 2025-11-

You are given a list of dictionaries representing students and their test scores.
Each dictionary contains:
- "name" (str): student's name
- "score" (int): their test score (0-100)

Write a function that groups students into grade categories:
- "A": score >= 90
- "B": score >= 80 and < 90
- "C": score >= 70 and < 80
- "D": score >= 60 and < 70
- "F": score < 60

Return a dictionary where keys are grade letters and values are lists of student names.
Only include grade categories that have at least one student.
Names within each category should maintain their original order from the input.

Example:
Input: 
[
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 82},
    {"name": "Charlie", "score": 58},
    {"name": "Diana", "score": 90},
    {"name": "Eve", "score": 75}
]

Output:
{
    "A": ["Alice", "Diana"],
    "B": ["Bob"],
    "C": ["Eve"],
    "F": ["Charlie"]
}

Constraints:
- 1 <= len(students) <= 100
- Student names are valid non-empty strings
- Scores are integers between 0 and 100
- No duplicate student names in input
"""

def group_by_grade(students):
    """
    Group students into grade categories based on their scores.
    
    Args:
        students: List of dicts with keys "name" and "score"
    
    Returns:
        Dict mapping grade letters to lists of student names
    """
    # Your code here
    grade_return = {}
    
    pass


# Test cases
if __name__ == "__main__":
    # Test 1: Basic case
    students1 = [
        {"name": "Alice", "score": 95},
        {"name": "Bob", "score": 82},
        {"name": "Charlie", "score": 58},
        {"name": "Diana", "score": 90},
        {"name": "Eve", "score": 75}
    ]
    
    # Test 2: All same grade
    students2 = [
        {"name": "John", "score": 85},
        {"name": "Jane", "score": 88},
        {"name": "Jack", "score": 81}
    ]
    
    # Test 3: Edge scores
    students3 = [
        {"name": "Min", "score": 0},
        {"name": "Max", "score": 100},
        {"name": "Boundary", "score": 90}
    ]
    
    print("Test 1:", group_by_grade(students1))
    # Expected: {"A": ["Alice", "Diana"], "B": ["Bob"], "C": ["Eve"], "F": ["Charlie"]}
    
    print("Test 2:", group_by_grade(students2))
    # Expected: {"B": ["John", "Jane", "Jack"]}
    
    print("Test 3:", group_by_grade(students3))
    # Expected: {"A": ["Max", "Boundary"], "F": ["Min"]}