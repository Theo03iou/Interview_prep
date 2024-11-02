# 1) Problem: Valid Anagram

# Description: Given two strings s and t, write a function to determine if t is an anagram of s.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# print(is_anagram("bat", "tab"))


# 2) Problem: First Unique Character in a String
# Description: Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

def first_unique_char(s: str) -> int:

    unique_dictionary = {}

    for character in s:
        if character in unique_dictionary:
            unique_dictionary[character] += 1
        else:
            unique_dictionary[character] = 1

    for index, cha in enumerate(s):
        if unique_dictionary[cha] == 1:
            return index

    return -1


# print(first_unique_char("poopsfsefs"))


# 3) Problem: Group Anagrams

# Description: Given an array of strings, group the anagrams together.
# You can return the answer in any order.

def groupAnagrams(str_array: list[str]) -> list[list[str]]:

    str_dictionary = {}

    for i in str_array:
        sorted_characters = sorted(i)
        sorted_key = ''.join(sorted_characters)

        if sorted_key not in str_dictionary:
            str_dictionary[sorted_key] = [i]
        else:
            str_dictionary[sorted_key].append(i)

    return list(str_dictionary.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
