# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# Lists are part of the collections family in python.
#creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5
print(len(my_list)) # 5
print(type(my_list)) # <class 'list'>
print(my_list[0]) # 1
print(my_list[1:4]) # [2, 3, 4]
print(my_list[1:]) # [2, 3, 4, 5]
print(my_list[:-1]) # [1, 2, 3, 4]
# reverse a list
print(my_list[::-1]) # [5, 4, 3, 2, 1]
#Modifying a list
my_list.append(6) # adds 6 to the end of the list
print(my_list) # [1, 2, 3, 4, 5, 6]
# add 7 and 8 to the end of the list
my_list.extend([7, 8])
print(my_list) #[1, 2, 3, 4, 5, 6, 7, 8]
my_list.extend ([9, 10, 11, 12])
print(my_list)
# remove the last item
my_list.pop(2)
print(my_list) 
# reverse the list
my_list.reverse()
print(my_list) # [7, 6, 5, 4, 2, 1]
#.remove to remove a specific value
my_list.reverse()
my_list.remove(4)
print(my_list)
my_list.remove(12)
print(my_list)
new_list = list(range(12, 120))
print(new_list)
my_list.append(new_list)
print(my_list)
new_list2 = list(range(120, 620))
my_list.append(new_list2)
print(my_list)
print(my_list[ : : 3])
print(my_list[ : : 10])
# Remove every third element in the list
del my_list[: : 3]
print(len(my_list))
print(my_list)

#list functions
# .append() - adds an item to the end of the list
# .extend() - adds multiple items to the end of the list
# .pop() - removes and returns an item at a given index
#  (default is the last item)
# .remove() - removes the first occurence of a specific value
# .sort() - sorts the list in ascending order
# .reverse() reverses the order of the list

# Why is a list more useful than a variable?
# A list can hold multiple values
# While a variable can only hold one at a time
cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)
# Access the first item
print(cakes[0])
# Access the last item
print(cakes[-1])
# Want to chocolate cake instead of vanilla
cakes[0] = 'strawberry'
print(cakes)
cakes[1] = 'chocolate'
# Add a new cake to the end of the list
cakes.append('lemon')
print(cakes)
cakes.pop()
print(cakes)
cakes.insert(2, 'funfetti')
print(cakes)

# Examples:

my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

my_list.pop(1)
print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
favorite_foods = ['Mozzarella sticks', 'Chocolate', 'Tacos', 'fried chicken', 'pizza']
# Print the second and last item.
print(favorite_foods[2])
print(favorite_foods[-1])
# Add a new item using .append().
favorite_foods.append('Cookies')
print(favorite_foods)
# Remove the first item using .pop(0).
favorite_foods.pop(0)
print(favorite_foods)
# Reverse your list using .reverse().
favorite_foods.reverse()
print(favorite_foods)
# Create a list of 3 lists (matrix), and access the middle element.
