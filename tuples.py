# A tuple is a collection type in python, similar to a list, except tuples are immutable. Meaning once created, it cant be changed

# 1. Creating a tuple

my_tuple = (1,2,3)

# Tuple can contain MULTIPLE data types
mixed_tuple = (42, "hello", 3.14, True)

# Single element tuple - just add a comma after the element
single_element_tuple = (5,)

# 2. Accessing Elements in a Tuple
my_tuple = (1,2,3)
print(my_tuple[1])

# 3. Reasons to Use Tuples: 
#   Immutability - Since they can't be modified, they're useful for data that should remain constant, like coordinates
#   Memory Efficiency - Tuples take up less memory compared to lists
#   Hashable - Tuples can be used as dictionary keys or stored in sets, unlike lists

# 4. Tuple Methods:
#   count(value): Counts how many times a specified value appears in the tuple
#   index(value): Find the index of the first occurence of the specified value

my_tuple = (1, 2, 2, 3, 4)
print(my_tuple.count(2))  # Output: 2
print(my_tuple.index(3))  # Output: 3

# 5. Tuple Unpacking:
#   You can assign each element of a tuple to separate variables
coordinates = (10, 20)
x, y = coordinates
print(x)
print(y)

# Practical Examples of Tuples:
#   Useful for grouping related values together, like pairs of names and ages
people = [("Alice", 25), ("Bob", 30), ("Dave", 45)]

for name, age in people:
    print(f"{name} is {age} years old")
    
# EXERCISE - Create a tuple with three numbers, then write a function that accepts this tuple as an argument and returns the sum of the numbers

my_tuple = (1,2,3)

def tupleSum(tup):
    x = 0
    for i in tup:
        x += i
    return x

print(tupleSum(my_tuple))