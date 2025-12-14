# Lists/Arrays Cheat Sheet

## Basics

### Creation & Access

```python
# creating
lst = []
lst = list()
lst = [1, 2, 3]
lst = list(range(5))

# Access
lst[0]   # First Item
lst[-1]  # Last Item
lst[-2]  # Second to last
lst[0:3] # Items 0-2
lst[:3]  # First 3 Items
lst[3:]  # 3 until the end of the list
lst[:]   # Copy of the entire list
```

### Adding Elements

```python
lst.append(item) # O(1)
lst.insert(0, item) # adding an item in a place in the list O(n)
                    # .append(item) -EQL-> lst.insert(len(lst), item)
lst.extend(lst_2) # O(k), k=len(lst2)
lst_3 = lst + lst_2 # Concatenates lists into a new list
```

### Removing Elements

```python
lst.pop() # O(1), removes last item
lst.pop(2) # index=2, O(n)
lst.remove(item) # remove frist occurrence of item - O(n)
del lst[1] # index=1, O(n)
lst.clear() # removes ALL elements
```

### Checking & Finding

```python
item in lst
lst.index(item) # just the first index, not index of all = values, Err
                # if not in, O(n)
lst.count(item) # count all occurrences - O(n)
len(lst) # entire len of list
```

### Sorting & Reversing

```python
# KEEPS OG LIST, just moving indexes
lst.sort()              # returns  lst = [1, 2, 3, 4, 5]
lst.sort(reverse=True)  # verses   lst = [5, 4, 3, 2, 1]
lst.reverse()           # lst = [5, 4, 3, 2, 1]

# CREATES NEW LIST, OG list doesn't change
lst_2 = sorted(lst)
lst_2 = reversed(lst)
```

## Common Patterns for Interview Problems

### Iterates with index
```python
""""
I have been using the classic 

for i in range(len(list)):
    print(f"{i} : {list[i]}")

but when looking things over it looks like enumerate seems to be suggested for readable code

It also has advantages when dealing with lists of dictionaries 
students = [
            {"name": "Spencer", "score": 91}, 
            {"name": "John", "score": 82},
            {"name": "Emily", "score": 97}
           ]

for i, student in enumerate(students):
    print(f"Student {i}: student["name"] scored {student["score"]}")

""""

for i, item in enumerate(lst):
    print(f"{i} : {item}")
```

### Iterate through two lists together
```python
names = ["Spencer", "Emily"]
scores = [95, 82]

for name, score in zip(names, scores):
    print(name, score)
```

### Building a new list (List Comprehension):

```python
"""
Instead of using `for loops in range` for squares or evens do it on one line
"""
squares = [x ** 2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
```


### Find min/max

```python
min(lst)
max(lst)
sum(lst)

# If in obj/dict
students = [
            {"name": "Spencer", "score": 91}, 
            {"name": "John", "score": 82},
            {"name": "Emily", "score": 97}
           ]

max(students, key=lambda s: s["score"]) # = "Emily"
```

### Two Pointer Technique
```python
"""
Need to check if sorted list has two numbers larger that sum to a set target. Return bool

given:

test_lst = [1, 2, 3]
test_sum = 5
expected result = False
"""

def two_sums_sorted(lst, target):
    left = 0
    right = len(lst) - 1

    while left < right:
        current_sum = lst[left] + lst[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return False
```

### Slicing tricks

```python
lst[::2] # every other element
lst[::-1] # crazy way to inverse list but interesting
lst[1::2] # every other stating at 1
```

### Copying lists

```python
lst_2 = lst # POINTS TO SAME LIST, NOT A COPY
```