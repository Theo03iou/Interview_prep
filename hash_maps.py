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

# print(student_ages.keys())
# print(student_ages.values())
# print(student_ages.items())

# Checking for a Key:
#   You can check if a key exists in a dictionary by using the *in* keyword

# print("Alice" in student_ages)
# print("Theo" in student_ages)


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


# print(wordCounter(sentences))


# The output should be a dictionary with word counts, like this:

# {"to": 2, "be": 2, "or": 1, "not": 1}


# SECOND EXERCISE

def first_unique_char(s):
    # Step 1: Initialize a dictionary for character counts
    character_count = {}
    # Step 2: Populate the dictionary with character counts
    for letter in s:
        if letter in character_count:
            character_count[letter] += 1
        else:
            character_count[letter] = 1
    print(character_count)

    for index, letter in enumerate(s):
        if character_count[letter] == 1:
            return index
    return -1

# Try testing with:
# print(first_unique_char("loveleetcode"))
# print(first_unique_char("aabb"))


# THIRD EXERCISE

# Given a list of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters...
# of a different word or phrase, typically using all the original letters exactly once.

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

# Output: [["bat"], ["ant", "tan"], ["ate", "eat", "tea"]]


def group_anagrams(strs):
    # Step 1: Initialize a dictionary to hold grouped anagrams
    anagrams = {}

    # Step 2: Iterate through the list of strings
    for string in strs:

        # Step 3: Sort the string to use as a key
        key = ''.join(sorted(string))

        # Step 4: Append the original string to the appropriate list in the dictionary
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(string)

    # Step 5: Return the values of the dictionary
    return list(anagrams.values())


# Test with an example
# print(group_anagrams(["eat", "tea", "tan", "ate", "ant", "bat"]))


# EXERCISE 4

# Problem: Character Frequency Count
# Description: Given a string, write a function that counts the frequency of each character in the string and returns a...
# dictionary with characters as keys and their frequencies as values.

def char_frequency(s: str) -> dict:
    frequency = {}

    for letter in s:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    return frequency


# print(char_frequency("poop"))


# EXERCISE 5

def word_frequency(sentence: str) -> dict:
    frequency = {}
    word_list = sentence.lower()
    word_list = word_list.split()

    for word in word_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# print(word_frequency("This is a test"))


# EXERCISE 6 -
# Given a list of integers, write a function that finds the integer that appears most frequently.
# If there’s a tie for the most frequent element, return the smallest integer among them.


def most_frequent(nums: list) -> int:
    
    num_dictionary = {}
    
    for num in nums:
        if num in num_dictionary:
            num_dictionary[num] += 1
        else:
            num_dictionary[num] = 1

    frequency = -1
    element = None
    
    for num, count in num_dictionary.items():
        if count > frequency or (count == frequency and num < element):
            frequency = count
            element = num

    # for i in num_dictionary:
    #     print(num_dictionary[i])
    #     if num_dictionary[i] > frequency:
    #         frequency = num_dictionary[i]
    #         element = i
    return element


print(most_frequent([1, 2, 3, 1, 2, 5, 3, 4, 1, 6]))
