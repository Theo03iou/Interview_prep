# A linked list is a data structure where each item (called a node) contains a value and a reference (or link) to the next node.
# It can be more memory-efficient than lists for certain operations, as items don't need to be stored contiguously in mremory

# Types of Linked-Lists:
#   Singly Linked List: Each node links only to the next node.
#   Doubly Linked List: Each node links to both the next AND previous node.
#   Circular Linked List: The last node linked back to the first node.

# Key Operations:
#   Insert: Add a node at the beginning, end of a specific operations.
#   Delete: Remove a node by value or position.
#   Traverse: Visit each node in sequence.

# Basic class to create and work with a singly linked list:

class Node:
    def __init__(self, data):
        self.data = data # Store the data of the node
        self.next = None # Pointer to the next node, initialised to None

class LinkedList:
    def __init__(self):
        self.head = None # Initialise the head of the list
    
    def insert(self, data):
        new_node = Node(data) # Create a new node
        if not self.head: # If the list is empty
            self.head = new_node # Set the new node as the head
        else: 
            current = self.head
            while current.next: # Traverse to the end of the list
                current = current.next
            current.next = new_node # Append the new node to the end of the list
            
    def delete(self, key):
        current = self.head
        previous = None
        while current: # Traverse the list
            if current.data == key: # Check if the current node has the data to delete
                if previous: # If its not the head
                    previous.next = current.next # Bypass the current node
                else:
                    self.head = current.next
                return
            previous = current # Move previous to current
            current = current.next # Move to the next node
            
    def traverse(self):
        current = self.head
        while current: # Traverse the list and print each node's data
            print(current.data)
            current = current.next

# Usage:

# Create a linked list and insert some elements
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)

# Traverse the linked list
linked_list.traverse()

# Delete a node
linked_list.delete(20)

# Traverse the linked list again
linked_list.traverse()



# Use Cases:
#   Dynamic Memory Allocation: Efficient memory usage, especially with frequent inserts and deletes
#   Implementation of Stacks and Queues: Linked lists are often used as the underlying structure
#   Graph and Tree Representations: Commonly used to store adjacency lists in graphs and in tree graphs