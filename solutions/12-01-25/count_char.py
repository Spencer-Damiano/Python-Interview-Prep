"""
Problem: Character Frequency Counter
Difficulty: Easy
Category: Hashmaps/Dictionaries
Date: 2024-11-18

You are given a string. Write a function that counts how many times each 
character appears in the string and returns a dictionary with the results.

The function should be case-sensitive (treat 'A' and 'a' as different characters).
Include spaces and punctuation in the count.
Return characters in the order they first appear in the string.

Example:
Input: "hello"
Output: {"h": 1, "e": 1, "l": 2, "o": 1}

Input: "Hello World!"
Output: {"H": 1, "e": 1, "l": 3, "o": 2, " ": 1, "W": 1, "r": 1, "d": 1, "!": 1}

Constraints:
- The string length can be anywhere from 0 to 1000 characters
- String may contain letters, digits, spaces, and punctuation
- Empty string should return empty dictionary
- Characters should appear in order of first occurrence
"""

def character_frequency(text):
    """
    Count the frequency of each character in the given string.
    
    Args:
        text: A string to analyze
    
    Returns:
        Dictionary mapping characters to their frequency counts,
        ordered by first appearance
    """
    char_map = {}

    if (0 <= len(text) >= 1000):
        print('ERROR: Word does not meet length requirements')
        return char_map
    

    for char in text:
        if char not in char_map:
            char_map[char] = 1
        elif char in char_map:
            char_map[char] += 1
    
    return char_map


# Test cases (don't look at these until you've attempted the problem!)
if __name__ == "__main__":
    # Test 1: Basic case with repeated characters
    test1 = "hello"
    
    # Test 2: Mixed case and spaces
    test2 = "Hello World!"
    
    # Test 3: Empty string
    test3 = ""
    
    # Test 4: All same character
    test4 = "aaaa"
    
    # Test 5: Numbers and special characters
    test5 = "abc123!@#123"
    
    result1 = character_frequency(test1)
    expected1 = {"h": 1, "e": 1, "l": 2, "o": 1}
    print(f'Test 1 passed: {result1 == expected1}')
    if result1 != expected1:
        print(f'  Got: {result1}')
        print(f'  Expected: {expected1}')
    
    result2 = character_frequency(test2)
    expected2 = {"H": 1, "e": 1, "l": 3, "o": 2, " ": 1, "W": 1, "r": 1, "d": 1, "!": 1}
    print(f'Test 2 passed: {result2 == expected2}')
    if result2 != expected2:
        print(f'  Got: {result2}')
        print(f'  Expected: {expected2}')
    
    result3 = character_frequency(test3)
    expected3 = {}
    print(f'Test 3 passed: {result3 == expected3}')
    if result3 != expected3:
        print(f'  Got: {result3}')
        print(f'  Expected: {expected3}')
    
    result4 = character_frequency(test4)
    expected4 = {"a": 4}
    print(f'Test 4 passed: {result4 == expected4}')
    if result4 != expected4:
        print(f'  Got: {result4}')
        print(f'  Expected: {expected4}')
    
    result5 = character_frequency(test5)
    expected5 = {"a": 1, "b": 1, "c": 1, "1": 2, "2": 2, "3": 2, "!": 1, "@": 1, "#": 1}
    print(f'Test 5 passed: {result5 == expected5}')
    if result5 != expected5:
        print(f'  Got: {result5}')
        print(f'  Expected: {expected5}')