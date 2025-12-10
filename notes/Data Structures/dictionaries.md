# Dictionary Cheat Sheet

## Basics

### Creation & Access
```python
# Creating
d = {}
d = dict()
d = {"key": "value"}

# Properly Access
d["key"]     # potential error
d.get("key") # None if missing
d.get("key") # 0 if Missing
```
### Adding/Updating
```python
d["key"] = value        # overrides the key
d.setdefault("key", []) # get existing value OR create key with a value
d.update({"k": "v"})    # merge another dict
```

### Accessing through loops
```python
for key in d: 
    return "Keys only"

for key, value in d.items():
    return "Key-Value pairs"

for value in d.values():
    return "Values only"

d.keys() # all keys as dict_keys objs
```

## Patterns for Interviews

### Counting
```python
""""
Use .get() as show below
The reason that I need to use the `counts[item]` is the same reason as
x = x * 2 w/o the x = it just does x * 2 w/o saving
""""

counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
```

### Grouping
```python

groups {}
for item in items:
    """"
    pretend that logic for determine the group that it is in here
    """"

    key = determine_group(item)
    unique_groups.getdefault(key, []).append(item)
    # grouping sets:
    # unique_groups.getdefault(key, set()).add(item)
```