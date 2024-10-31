
# 4. Common List Methods
#   Adding Elements:
#       append(item): adds an item to the end of the list
#       insert(index, item): Inserts an item at a specified index

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "kiwi")

#   Removing Elements:
#       remove(item): Removes the first occurence of the specified item
#       pop(index): Removes and returns the item at the specified index (or the last item if no index is specified)

fruits.remove("cherry")
last_fruit = fruits.pop()

#   Finding Length and other useful methods:
#       len(list): Returns the number of elements in the list
#       count(item): Returns the number of occurrences of item
#       index(item): Returns the index of the first occurrence of item

num_fruits = len(fruits)
kiwi_count = fruits.count("kiwi")
kiwi_index = fruits.index("kiwi")


#  5. Slicing lists

sublist = fruits[1:3]

# 6. List Comprehensions

# Provide a concise way to create lists, can also include conditions

squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)


# EXAMPLE EXERCISE - Remove duplicates from a list

# Given a list of integers,
# write a function that removes duplicates and returns a new list containing only unique elements,
# maintaining the order of their first appearance

numbers = [1, 2, 3, 2, 4, 1, 5]


def duplicate_tracker(y):
    new_list = []
    for x in y:
        if x not in new_list:
            new_list.append(x)
    return new_list


print(duplicate_tracker(numbers))
