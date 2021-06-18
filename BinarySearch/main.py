from binary_search_recursive import binary_search_rec
from binary_search_iterative import binary_search_iter

# Provide a sorted array and an item to be searched.
# arr = [1,2,3,4][]
# item = 2 

arr = [2, 3, 7, 12, 17, 24, 35, 42]
item = 42

# # Recursive Call for Binary Search 
# print("Using Recursion:")
# print(binary_search_rec(arr, item, 0, len(arr) - 1))

# Iterative Call for Binary Search
print("Using Iteration:")
print(binary_search_iter(arr, item))

# # Both above function can also be called as:

# print(binary_search_rec([12,45,56,89,96], 56, 0, 4))
# print(binary_search_iter([12,45,56,89,96], 56))

# But these are considered as hard coded, so avoid this practice.