"""
Problem: Merge Sorted Gift Lists
Difficulty: Easy
Category: Arrays/Two Pointers
Date: CHRISTMAS

You're helping organize gift distribution at a charity event. Two volunteers 
have each created sorted lists of gift recipient IDs (sorted in ascending order).
You need to merge these two lists into one sorted list.

The lists represent the order gifts should be distributed, and you need to 
maintain the sorted order in the final combined list.

Example 1:
Input: 
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
Output: 
    [1, 2, 3, 4, 5, 6, 7, 8]

Example 2:
Input:
    list1 = [1, 2, 9]
    list2 = [3, 4, 5]
Output:
    [1, 2, 3, 4, 5, 9]

Example 3:
Input:
    list1 = []
    list2 = [1, 2, 3]
Output:
    [1, 2, 3]

Constraints:
- 0 <= len(list1), len(list2) <= 100
- Both input lists are already sorted in ascending order
- All recipient IDs are non-negative integers
- Lists may be empty
- Lists may have different lengths
"""

def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list.
    
    Args:
        list1: First sorted list of integers
        list2: Second sorted list of integers
    
    Returns:
        New sorted list containing all elements from both input lists
    """
    # Your code here
    pass


# Test cases (don't look at these until you've attempted the problem!)
if __name__ == "__main__":
    # Test 1: Equal length lists with interleaved values
    list1_a = [1, 3, 5, 7]
    list2_a = [2, 4, 6, 8]
    
    # Test 2: Different length lists
    list1_b = [1, 2, 9]
    list2_b = [3, 4, 5]
    
    # Test 3: One empty list
    list1_c = []
    list2_c = [1, 2, 3]
    
    # Test 4: Both lists empty
    list1_d = []
    list2_d = []
    
    # Test 5: One list exhausts first
    list1_e = [1, 2, 3]
    list2_e = [4, 5, 6, 7, 8]
    
    # Test 6: Lists with duplicate values
    list1_f = [1, 3, 3, 5]
    list2_f = [2, 3, 4]
    
    print("Test 1:", merge_sorted_lists(list1_a, list2_a))
    # Expected: [1, 2, 3, 4, 5, 6, 7, 8]
    
    print("Test 2:", merge_sorted_lists(list1_b, list2_b))
    # Expected: [1, 2, 3, 4, 5, 9]
    
    print("Test 3:", merge_sorted_lists(list1_c, list2_c))
    # Expected: [1, 2, 3]
    
    print("Test 4:", merge_sorted_lists(list1_d, list2_d))
    # Expected: []
    
    print("Test 5:", merge_sorted_lists(list1_e, list2_e))
    # Expected: [1, 2, 3, 4, 5, 6, 7, 8]
    
    print("Test 6:", merge_sorted_lists(list1_f, list2_f))
    # Expected: [1, 2, 3, 3, 3, 4, 5]