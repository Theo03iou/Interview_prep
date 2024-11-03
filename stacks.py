# A STACK is a Last in, First Out (LIFO) data structure. It works like a stack of plates:
# the last item you put on the stack is the first item you take off

# Key operations

# Push: Add an item to the top of the stack
# Pop: Remove and return the top item
# Peek: View the top item without removing it
# Is Empty: Check if the stack is empty

# Stacks are often implemented using lists

stack = [] 
stack.append(1) # Push
stack.append(2)
top_item = stack.pop() # Pop (return 2)
print(stack) 

# Use Cases

# Backtracking: Undo actions in editors, navigations, etc.
# Parsing: Checking if parentheses in an expression are balanced
# Recursive Algorithms: Implement recursion iteratively