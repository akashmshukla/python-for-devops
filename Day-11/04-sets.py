my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Adding an element
my_set.remove(3)  # Removing an element

print(my_set)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)  # Union of sets
print(union_set)

intersection_set = set1.intersection(set2)  # Intersection of sets
print(intersection_set)

difference_set = set1.difference(set2)  # Difference of sets
print(difference_set)

is_subset = set1.issubset(set2)  # Checking if set1 is a subset of set2
print(is_subset)
is_superset = set1.issuperset(set2)  # Checking if set1 is a superset of set2
print(is_superset)

set3 = {2,3}

is_subset = set3.issubset(set1)  # Checking if set1 is a subset of set2
print(is_subset)
is_superset = set3.issuperset(set1)  # Checking if set1 is a superset of set2
print(is_superset)
is_subset = set3.issubset(set2)  # Checking if set1 is a subset of set2
print(is_subset)
is_superset = set3.issuperset(set2)  # Checking if set1 is a superset of set2
print(is_superset)