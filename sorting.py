
# 1. Sorting with sorted() and list.sort()

# sorted(): A built-in function that creates and returns a new sorted list from any iterable (e.g., lists, tuples).
# list.sort(): A method that sorts the list in place and doesn’t return a new list.

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
# OR
numbers.sort()


# 2. Sorting order

# By default, both sorted() and list.sort() sort elements in ascending order.
# To sort in descending order, use the parameter reverse=True.

sorted_desc = sorted(numbers, reverse=True)


# 3. Sorting with key and lambda functions

# The key parameter allows you to specify a function to transform each item before sorting.
# Lambda functions (inline functions) are often used with key to define sorting rules concisely.

pairs = ['cherry', 'banana','pair', 'apple']
sorted_by_length = sorted(pairs, key=lambda x: len(x))
# print(sorted_by_length)


# 4. Sorting complex data (e.g tuples, dictionaries)

# For lists of tuples, you can sort by specific tuple elements using key

pairs = [(2, 'cherry'), (4, 'banana'), (1, 'pair'), (1, 'apple')]
sorted_pairs = sorted(pairs, key=lambda x: x[0])
# print(sorted_pairs)


# 5. Using operator for a more complex sorts

# For more readable sorting, the operator module offers functions that work well as key arguments, such as operator.itemgetter() for tuples and dictionaries

# e.g. Sorting a list of dictionaries by a specific field:

from operator import itemgetter

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

sorted_students = sorted(students, key=itemgetter('grade'), reverse=True)
# print(sorted_students)



# SORTING EXERCISE

# Exercise: Sorting Names by Last Name and Length
# Given a list of full names, sort the list first by last name alphabetically and then by the length of the full name in ascending order. 
# If two names have the same last name and length, their original order should be preserved (stable sort).

# Expected Output: After sorting, the list should be ordered alphabetically by last name and then by the length of each name.

# Hint: Use sorted() with a key that accesses both the last name and the length of each name.

names = ["John Doe", "Jane Smith", "Alice Johnson", "Chris Doe", "Eve Smith"]

