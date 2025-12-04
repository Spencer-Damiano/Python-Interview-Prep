"""
Problem: Count Word Frequency
Difficulty: Easy
Category: Hashmaps/Dictionaries
Date: 2025-12-03

You are given a list of words (all lowercase, no punctuation).
Count how many times each word appears in the list.

Return a dictionary where:
- Keys are the words
- Values are the counts (how many times that word appeared)

Example:
Input: ["apple", "banana", "apple", "cherry", "banana", "apple"]
Output: {"apple": 3, "banana": 2, "cherry": 1}

Example 2:
Input: ["hello", "world"]
Output: {"hello": 1, "world": 1}

Constraints:
- 1 <= len(words) <= 100
- All words are lowercase strings
- No empty strings
- Words may repeat
"""

def count_words(words):
    """
    Count the frequency of each word in the list.
    
    Args:
        words: List of strings (all lowercase)
    
    Returns:
        Dict mapping each word to its count
    """
    # Your code here
    pass


# Test cases (don't look until you've attempted!)
if __name__ == "__main__":
    # Test 1: Basic case with duplicates
    test1 = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    
    # Test 2: No duplicates
    test2 = ["hello", "world"]
    
    # Test 3: All same word
    test3 = ["cat", "cat", "cat", "cat"]
    
    # Test 4: Single word
    test4 = ["solo"]
    
    print("Test 1:", count_words(test1))
    # Expected: {"apple": 3, "banana": 2, "cherry": 1}
    
    print("Test 2:", count_words(test2))
    # Expected: {"hello": 1, "world": 1}
    
    print("Test 3:", count_words(test3))
    # Expected: {"cat": 4}
    
    print("Test 4:", count_words(test4))
    # Expected: {"solo": 1}