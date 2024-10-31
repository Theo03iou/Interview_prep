# A dictionary is an unordered collection of key-value pairs. Keys are unique, and they allow you to access values efficiently.
# Dictionaries are very useful for counting, grouping data, and fast lookups

# 1. Creating a dictionary

student_ages = {"Alice": 21, "Bob": 22, "Charlie": 23}
# OR
student_ages = dict(Alice=21, Bob=22, Charlie=23)


# 2. Accesssing and Modifying Values

# You can access, add, or modify using keys

# Accessing a value
# print(student_ages["Alice"])
# Adding or modifying a value
student_ages["Alice"] = 25
student_ages["David"] = 20      # Adds a new entry for David

# 3. Common Dictionary Methods

# Adding and Removing Elements:
#   dict[key] = value: Adds or updates a key-value pair
#   pop(key): Removes and returns the value of a specified key
#   del dict[key]: Deletes the specified key value-pair

student_ages.pop("Bob")
del student_ages["Charlie"]

# Getting All Keys, Values, and Items:
#   keys(): returns all keys
#   values(): returns all values
#   items(): returns all key-value pairs as tuples in a list.

print(student_ages.keys())
print(student_ages.values())
print(student_ages.items())

# Checking for a Key:
#   You can check if a key exists in a dictionary by using the *in* keyword

print("Alice" in student_ages)
print("Theo" in student_ages)


# 4. Dictionary Comprehension:

# Similar to list comprehensions, you can create dictionaries using a concise syntax

squares = {x: x**2 for x in range(1, 6)}
# print(squares)


# Use cases for Dictionaries

# Dictionaries are incredbily useful for:
#   Counting Occurences
#   Mapping data
#   Grouping items by a key


# EXAMPLE EXERCISE - Count Word Frequency

# Write a function that takes a sentence (string) and returns a dictionary with word counts, like this

sentences = "to be or not to be"


def wordCounter(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = True

    return word_count


print(wordCounter(sentences))


# The output should be a dictionary with word counts, like this:

# {"to": 2, "be": 2, "or": 1, "not": 1}
