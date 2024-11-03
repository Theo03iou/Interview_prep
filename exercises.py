# 1) Problem: Valid Anagram

# Description: Given two strings s and t, write a function to determine if t is an anagram of s.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

import heapq


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
# print(groupAnagrams(strs))


# 4). Problem: Top K Frequent Elements

# Given a list of integers, return the k most frequent elements.
# You may assume that k is always a valid integer (between 1 and the number of unique elements in the list).


def top_k_frequent(nums: list[int], k: int) -> list[int]:

    num_dictionary = {}

    for num in nums:
        if num in num_dictionary:
            num_dictionary[num] += 1
        else:
            num_dictionary[num] = 1

    min_heap = []

    for num, count in num_dictionary.items():
        heapq.heappush(min_heap, (count, num))
        print(min_heap)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    top_k = [num for count, num in min_heap]

    return top_k


# print(top_k_frequent([4, 4, 4, 4, 2, 2, 3, 3, 3, 5], 3))


# 5). Problem: Valid Anagram

# Given two strings s and t, write a function to determine if t is an anagram of s.

def is_anagram(s: str, t: str) -> bool:
    anagram_dictionary = {}

    for s_letter in s:
        if s_letter in anagram_dictionary:
            anagram_dictionary[s_letter] += 1
        else:
            anagram_dictionary[s_letter] = 1

    for t_letter in t:
        if t_letter in anagram_dictionary:
            anagram_dictionary[t_letter] -= 1


    # Check if all values in the dictionary are zero
    for count in anagram_dictionary.values():
        if count != 0:
            return False
    return True


print(is_anagram("anagram", "nagaram"))  # Expected output: True
print(is_anagram("rat", "car"))          # Expected output: False
