my_set={1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = { 4, 5,3,7}

# union of two sets
union_set = set1.union(set2)
union_set = set1 | set2  # Using the '|' operator for union
print(union_set)  # Output: {1, 2, 3, 4, 5}

# intersection of two sets
intersection_set = set1.intersection(set2)
intersection_set = set1 & set2  # Using the '&' operator for intersection
print(intersection_set)  # Output: {3}

# difference of two sets
difference_set = set1.difference(set2)
difference_set = set1 - set2  # Using the '-' operator for difference
print(difference_set)  # Output: {1, 2}

# symmetric difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2)
symmetric_difference_set = set1 ^ set2  # Using the '^' operator for symmetric difference
print(symmetric_difference_set)  # Output: {1, 2, 4, 5, 7}