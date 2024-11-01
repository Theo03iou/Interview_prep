# 1. What is a Heap?
#   A heap is a specialised binary tree-based data structure that satifies the heap property:
#       In a min-heap, the smallest element is always at the root (top).
#       In a max-heap, the largest element is always at the root (top).
# Python's built in heapq module implements a min-heap, where the smallest element can be accessed or removed quickly

# 2. Converting a List into a Heap
# To turn a list into a heap, use heapq.heapify()

import heapq
numbers = [4, 7, 2, 9, 1]
heapq.heapify(numbers)

# After heapify, numbers is now structured as a heap, where the smallest element (1) is at the root

# 3. Common heapq Operations:
#   Push(Add) an Element: heapq.heappush(heap, item) adds item to the heap
heapq.heappush(numbers, 13)
heapq.heappush(numbers, 3)

# Pop(Remove) the Smallest Element: heapq.heappop(heap) removes and returns the smallest element
smallest = heapq.heappop(numbers)
print(smallest)

# Push and Pop Together: heapq.heappushpop(numbers, 5), efficiently pushes an item on and pops the smallest item off in a single operation
smallest = heapq.heappushpop(numbers, 12)
print(smallest)
print(numbers)

# 5. Practical Use Case for Heaps:
#   Heaps are ideal for situations like finding the k smallest or k largest elements from a large dataset
#   E.G. if you need the 3 smallest numbers from a list, you can use heapq.smallest():
numbers = [10, 20, 15, 5, 30, 25]
smallest_three = heapq.nsmallest(3, numbers)
print(smallest_three)

# EXERCISE - Given a list of numbers, use a heap to find the two smallest elements.

nums = [1, 2, 3, 4, 5, 6]
smallest_two = heapq.nsmallest(2, nums)
print(smallest_two)
