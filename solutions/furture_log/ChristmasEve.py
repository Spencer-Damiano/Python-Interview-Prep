"""
Problem: Filter the Naughty List
Difficulty: Easy
Category: Arrays/Sets
Date: 2024-12-25

Santa needs help! He has a list of children who should receive gifts, but
he also has a naughty list of children who shouldn't get presents this year.

Given a list of children's names and a naughty list, return only the names
of children who are NOT on the naughty list (the nice kids who should get gifts).

The returned list should maintain the original order from the input list.

Example 1:
Input: 
    children = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    naughty_list = ["Bob", "Eve"]
Output: 
    ["Alice", "Charlie", "Diana"]

Example 2:
Input:
    children = ["Emma", "Liam", "Olivia"]
    naughty_list = ["Sophia"]
Output:
    ["Emma", "Liam", "Olivia"]

Example 3:
Input:
    children = ["Noah", "Ava"]
    naughty_list = ["Noah", "Ava"]
Output:
    []

Constraints:
- 0 <= len(children) <= 1000
- 0 <= len(naughty_list) <= 1000
- All names are non-empty strings
- Names are case-sensitive
- A child's name may appear multiple times in the children list
- A name on the naughty list should exclude ALL occurrences from children list
- Names in naughty_list are unique
"""

def filter_naughty_list(children, naughty_list):
    """
    Filter out children who are on the naughty list.
    
    Args:
        children: List of children's names (may contain duplicates)
        naughty_list: List of names on the naughty list
    
    Returns:
        List of names not on the naughty list, maintaining original order
    """
    # Your code here
    pass


# Test cases (don't look at these until you've attempted the problem!)
if __name__ == "__main__":
    # Test 1: Basic filtering
    children1 = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    naughty1 = ["Bob", "Eve"]
    
    # Test 2: No one on naughty list
    children2 = ["Emma", "Liam", "Olivia"]
    naughty2 = ["Sophia"]
    
    # Test 3: Everyone on naughty list
    children3 = ["Noah", "Ava"]
    naughty3 = ["Noah", "Ava"]
    
    # Test 4: Empty children list
    children4 = []
    naughty4 = ["Mason"]
    
    # Test 5: Empty naughty list
    children5 = ["Lucas", "Mia"]
    naughty5 = []
    
    # Test 6: Duplicate names in children list
    children6 = ["Zoe", "Leo", "Zoe", "Ella", "Leo"]
    naughty6 = ["Leo"]
    
    # Test 7: Case sensitivity matters
    children7 = ["anna", "Anna", "ANNA"]
    naughty7 = ["Anna"]
    
    print("Test 1:", filter_naughty_list(children1, naughty1))
    # Expected: ["Alice", "Charlie", "Diana"]
    
    print("Test 2:", filter_naughty_list(children2, naughty2))
    # Expected: ["Emma", "Liam", "Olivia"]
    
    print("Test 3:", filter_naughty_list(children3, naughty3))
    # Expected: []
    
    print("Test 4:", filter_naughty_list(children4, naughty4))
    # Expected: []
    
    print("Test 5:", filter_naughty_list(children5, naughty5))
    # Expected: ["Lucas", "Mia"]
    
    print("Test 6:", filter_naughty_list(children6, naughty6))
    # Expected: ["Zoe", "Zoe", "Ella"]
    
    print("Test 7:", filter_naughty_list(children7, naughty7))
    # Expected: ["anna", "ANNA"]