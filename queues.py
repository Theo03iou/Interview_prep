# A queue is a First In, First Out (FIFO) data structure.

# Key Operations:

# Enqueue: Add an item to the end of the queue
# Dequeue: Remove and return the item at the front
# Peek: View the front item without removing it
# Is Empty: Check if the queue is empty

# Queues are often implemented using collections.dequeue, which allows efficient appending and popping from both ends

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
front_item = queue.popleft() # Dequeue, returns 1
print(queue)

# Use Cases:
#   Order Processing: Managing tasks, customer orders, etc
#   BFS: Used in graphs and tree traversal
#   Producer-Consumer Problems: Efficiently handling tasks in systems where some components generate tasks, and others complete them