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


# print(is_anagram("anagram", "nagaram"))  # Expected output: True
# print(is_anagram("rat", "car"))          # Expected output: False


# 6). Problem 1: Count Element Frequencies

# Write a function that takes a list of integers and returns a dictionary where each key is an integer from the list,
# and the value is the number of times that integer appears.

def freq_counter(intList: list[int]) -> dict[int, int]:
    freq_dict = {}

    for num in intList:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    return freq_dict


# print(freq_counter([1, 2, 3, 1, 2, 3, 4, 5, 3]))


# Problem 2: First Non-Repeating Character
# Problem: Given a string, return the index of the first non-repeating character. If all characters are repeating, return -1.

def non_repeat(string: str):

    dictionary = {}

    for char in string.lower():
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    for index, char in enumerate(string.lower()):
        if dictionary[char] == 1:
            return index
    return -1


# print(non_repeat("Polop"))


# Problem 3: Two-Sum Problem

# Problem: Write a function that takes a list of integers and a target integer.
# Return the indices of the two numbers that add up to the target.
# Example: For nums = [2, 7, 11, 15] and target = 9, return [0, 1].

def two_sum(intList: list[int], target: int) -> list:

    int_dictionary = {}

    for index, num in enumerate(intList):
        complement = target - num
        if complement in int_dictionary:
            return [int_dictionary[complement], index]
        int_dictionary[num] = index
    return -1


# print(two_sum([13, 6, 5, 4, 11, 15, 3], 10))


# Problem 4: Check for Anagram

# 	•	Problem: Write a function that takes in two strings and checks if one string is an anagram of
#                the other.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashy = {}

        for i in strs:
            sorted_word = "".join(sorted(i))
            if sorted_word in hashy:
                hashy[sorted_word].append(i)
            else:
                hashy[sorted_word] = [i]

        return list(hashy.values())


# Sample input
test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Create an instance of the Solution class
solution = Solution()

# Function call
# print(solution.groupAnagrams(test_input))


# Problem 5: Find Longest Substring Without Repeating Characters

# 	•	Problem: Write a function that takes a string and finds the length of the longest substring with
#                all unique characters.
# 	•	Hint: Use a hash map to track the last seen position of each character.


# Practice Problem: Portmanteau Word Finder

# Problem Description:

# Write a function that takes a list of words and finds the longest “portmanteau” word.
# A portmanteau word is a word that is created by combining two smaller words from the list.
# The portmanteau word must be formed by taking the prefix from one word and the suffix from another word.

# 	1.	A word is a “prefix” of another if it starts the word (e.g., “auto” is a prefix of “automatic”).
# 	2.	A word is a “suffix” of another if it ends the word (e.g., “matic” is a suffix of “automatic”).

# The function should return the longest portmanteau word found in the list, or None if no portmanteau word can be formed.


def find_longest_portmanteau(strs: list[str]) -> str:
    word_list = set(strs)
    highest = ""
    for j in range(len(strs)):
        for i in range(j+1,len(strs)):
            new_word = strs[j] + strs[i]
            if new_word in word_list:
                if len(new_word) l> len(highest):
                    highest = new_word
    if highest != "":        
        return highest
    else:
        return "Not valid"
    
                    
            
    return "Doesn't exist"

    word_list = set(strs)
    
    for word1 in word_list:
        for all_Words in word_list:
            new_word = word1 + all_Words
            if new_word in word_list:
                return new_word
    return "Doesn't exist"

words = ["auto", "mobile", "photo", "matic", "automate", "automobile", "ation", "graphss", "photographss", "mobilephone", "phone", "mobilemobile"]

# print(find_longest_portmanteau(words))

words1 = ["auto", "matic", "automobile", "graph", "graphite"]
# Expected: "automatic" (auto + matic)

words2 = ["photo", "graph", "photograph", "auto", "matic"]
# Expected: "photograph" (photo + graph)

words3 = ["car", "pet", "carpet", "cap", "per"]
# Expected: "carpet" (car + pet)

words4 = ["swim", "ming", "swimming", "ball", "balling"]
# Expected: "swimming" (swim + ming)

print("words " + find_longest_portmanteau(words))
print("words2 " + find_longest_portmanteau(words2))
print("words3 " + find_longest_portmanteau(words3))
print("words4 " + find_longest_portmanteau(words4))