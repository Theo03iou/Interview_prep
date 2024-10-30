
# 1. String basics

# Strings in python are immutable sequences of characters, meaning once a string is created, it cant be changed.
# To make any modifications, you need to create a new string

text = "hello"


# 2. Accessing characters and slices

# Access individual characters by their index.
# Negative indexing allows you to count them from the end.
# Slice strings to get substrings using string[start:end]

text = "hello"
# print(text[0])
# print(text[-1])
# print(text[1:2])
# print(text[2:4])


# 3. Common string methods

# Basic manipulation:
#   upper() / lower(): Convert to uppercase or lowercase
#   strip(): Removes leading and trailing whitespaces
#   replace(old, new): Replaces all instances of old with new

text = "    Hello World   "
# print(text.strip())
# print(text.replace("World", "Poop"))

# Splitting and Joining:
#   split(): Splits the string into a list based on a delimiter (default is a whitespace)
#   join(): Joins elements of a list into a string with a specified separator

sentence = "Hello world, how are you?"
words = sentence.split()
# print(words)
# print("-".join(words))

# Finding and Counting:
#   find(substring): Returns the first index where substring is found, or -1 if not found
#   count(substring): Counts occurrences of substring in the string

text = "banana"
# print(text.find("na"))
# print(text.count("a"))


# 4. Checking conditions:
#   startswith() / endswith(): Checks if the string starts or ends with a specific substring
#   isalpha() / isdigit() / isalnum(): Check if the string consists only of letters, digits, or both.

word = "python3"
# print(word.isalpha())
# print(word.isalnum())


# 5. Reversing Strings:
#   The simplest way to reverse a string is to use slicing with [::-1]

text = "hello"
# print(text[::-1])


# 6. Advanced String Manipulation with format() and f-strings:
#   You can use format() or f-strings to create dynamic strings easily
#   f-strings are generally preferred for readaility and performance

name = "Theo"
age = 20
# print("My name is {}, and I am {} years old".format(name, age))
# print(f"My name is {name}, and I am {age} years old")



# EXAMPLE EXERCISE  -  Check if two strings are anagrams

# Given two strings, determine if they are anagrams

str1 = "listen"
str2 = "sildent"

str1, str2 = str1.lower(), str2.lower()
def sortFunc(a, b):
    return sorted(a) == sorted(b)

print(sortFunc(str1, str2))


