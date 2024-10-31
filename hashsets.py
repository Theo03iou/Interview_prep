# Sets are an unordered collection of unique elements. Particularly useful for operations that involve membership testing, removing duplicates, and performing mathematical set operations like union, intersection, etc.

# Creating a set

fruits = {"apple", "banana", "cherry"}
# Alternatively
numbers = set([1, 2, 3, 4, 5])


# 2. Accessing Elements

# Unlike lists, sets do not support indexing or slicing because they are unordered
# You can iterate through them of check for membership

print("banana" in fruits)  # True
print("orange" in fruits)  # False


# 3. Adding and Removing Elements

# You can add elements using add() and remove them using remove() or discard()

fruits.add("orange")
fruits.remove("banana")  # Removes banana and DOES raise an error if not found
# Removes banana and DOESN'T raise an error if not found
fruits.discard("banana")


# 4. Set Operations

# Sets support multiple mathematical operations
#   Union (|) combines elements from both sets
#   Intersection (&) returns elements that are in both sets
#   Difference (-) returns elements that are in the first set but not in the second
#   Symmetric Difference (^) returns elements that are in either of the sets but not in both

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
print(set_a ^ set_b)


# 5. Commmon set methods

# len(set): Returns the number of elements in the set
# clear(): Removes all elements from the set
# copy(): Returns a shallow copy of the set

print(len(fruits))
fruits.clear()


# EXAMPLE EXERCISE - Write a function that takes a list of integers and returns a set of unique elements from the list

numbers = [1,2,2,3,4,4,5,1]

def intfunc(int_list):
    new_set = set(int_list)
    return new_set
    
    
print(intfunc(numbers))