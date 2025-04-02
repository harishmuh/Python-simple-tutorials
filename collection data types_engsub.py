# Collection Data Types

# ===========
# [list]
# ===========
# Square brackets []
# A list is like a box that can hold items/elements of various data types (int, string, float, boolean, list).
# Allows duplicate values.
# Mutable, meaning items in a list can be modified, added, or removed.
# Ordered and indexed, so indexing and slicing can be performed.

# =============

# 1. Can contain items/elements of various data types
example_list = ['hello', 3, 2, 1, True]
# print(example_list)

nested_list = ['hello', 1, 2, 3, False, [4, 5, 6], example_list]
# print(nested_list)

# =========================
# 2. Allows duplicate values
example_list_1 = ['hello', 3, 2, 1, True, 6, 6, 6]
# print(example_list_1)

# ===========================
# 3. Ordered, so indexing and slicing can be performed
nested_list = ['hello', 1, 2, 3, False, [4, 5, 6], example_list]

# Indexing
print('Index 2:', nested_list[2])

# Slicing
print(nested_list[::2])

# ================================
# 4. Mutable, list items can be modified

nested_list[5][1] = '30'
print(nested_list)  # ['hello', 1, 2, 3, False, [4, '30', 6], example_list]

#================================================
# Membership Operator
# Check if a value exists in a list (in & not in)

example_list = ['Hello', 3, 2, False, True, [10, 20, 30], 6, 6, 6]

print('Hello' in example_list)           # True
print(20 in example_list)                # False
print(20 in example_list[5])             # True
print([10, 20, 30] in example_list)      # True
print(6 in example_list)                 # True
print(1 in example_list)                 # True (True is treated as 1)
print(0 in example_list)                 # True (False is treated as 0)

#=========================================
# Checking index in a list

# print(example_list.index(20))          # Error → 20 is not in the list
print(example_list.index(6))             # Shows the first occurrence of 6: index 6
print(example_list.index(0))             # False is treated as 0
print(example_list.index(1))             # True is treated as 1
print(example_list.index([10, 20, 30]))  # [10, 20, 30] is at index 5
print(example_list[5].index(20))         # 20 is at index 1 in example_list[5]
print(example_list[example_list.index([10, 20, 30])].index(20))  # 20 is at index 1 in example_list[5]
print([10, 20, 30].index(20))            # 20 is at index 1 in [10, 20, 30]

#==================================================
# Indirect Assignment

a = 100
b = 200

a = b

a = 500

print(a)
print(b)

#-----------------------

list_a = [10, 20, 30, 40]
list_b = list_a

print('Initial list_a:', list_a)
print('Initial list_b:', list_b)

list_b[-1] = 100
print('Final list_b:', list_b)
print('Final list_a:', list_a)

#-------------------------
# Use .copy() so the original list_a does not change
print('------.copy()------')

list_a = [10, 20, 30, 40]
list_b = list_a.copy()

print('Initial list_a:', list_a)
print('Initial list_b:', list_b)

list_b[-1] = 100
print('Final list_b:', list_b)   # The last item in list_b is changed
print('Final list_a:', list_a)   # The last item in list_a remains unchanged

# ======================================
# List Concatenation
# ======================================

#==============================================
# Adding items/elements to a list

# append: adds one item to the list
cars = ['toyota', 'vw', 'honda']
new_car = 'lamborghini'

cars.append(new_car)  # Cannot be assigned to a variable
print(cars)
print(len(cars))

# extend: adds multiple items separately
cars = ['toyota', 'vw', 'honda']
new_cars = ['lamborghini', 'nissan']

cars.extend(new_cars)
print('Using extend:', cars)  # ['lamborghini', 'nissan'] are added separately
print(len(cars))

# insert: inserts an item at a specific position
cars.insert(0, new_cars)
print('Using insert:', cars)  # ['lamborghini', 'nissan'] inserted at index 0 as a single list
print(len(cars))

# ==================================
# Tuple

# Denoted by parentheses ()
# Similar to lists, can store different data types
# Allows duplicate items
# Ordered, so indexing and slicing can be performed
# Immutable, meaning tuple items cannot be changed

tuple_example = ('Hello', 3, 2, 1, True, [10, 20, 30], 6, 6, 6)
print(tuple_example)

# Indexing and slicing
print(tuple_example[1])    # 3
print(tuple_example[1:5])  # (3, 2, 1, True)

# Immutable
# tuple_example[1] = 'Hi'  # Error → 'tuple' object does not support item assignment

# If we need to modify a tuple:
list_example = list(tuple_example)
list_example[1] = 'Hi'
tuple_example = tuple(list_example)
print(tuple_example)

#---------------------------------
# Adding items to a dictionary

dict_example = {
    'Name': ['Ridwan', 'Boni'],
    'Age': [25, 23],
    'Program': 'Data Science',
    'Status': 'secret',
}

# Adding an item
dict_example['Hobby'] = ['Reading', 'Swimming']
print(dict_example)

# Adding multiple items
dict_example.update({'Location': 'Bandung', 'Dreams': ['Data Scientist', 'Data Analyst']})
print(dict_example)

# Deleting an item
del dict_example['Status']
print(dict_example)

#======================================================
# Dictionary menu-based program

my_dict = {
    'milk': {'brand': 'ultra', 'price': 5000},
    'instant noodles': {'brand': 'indomie', 'price': 3000},
    'cooking oil': {'brand': 'bimoli', 'price': 36000}
}

while True:
    print('''Menu Options:
    1. Add a product
    2. Remove a product
    3. Exit
    ''')

    choice = input('Enter menu (1/2/3): ')

    if choice == '1':
        product = input('Enter product: ')
        brand = input('Enter brand: ')
        price = int(input('Enter price: '))
        my_dict[product] = {'brand': brand, 'price': price}
        print('Data successfully added:', product, ':', my_dict[product])
        print(my_dict)
    elif choice == '2':
        product = input('Enter product to remove: ')
        del my_dict[product]
        print(my_dict)
    elif choice == '3':
        print('Thank you!')
        break
    else:
        print('Please enter a valid option.')

#===================================================
# SET

# Denoted by curly braces {}
# Stores different data types
# Cannot contain duplicate items
# Unordered, so indexing is not possible
# Mutable
# Often used to remove duplicates

set_example = {'Hello', 3, 2, 1, True, 6, 6, 6}
print(set_example)

# Looping through a set
for item in set_example:
    print(item)

# Removing an item
set_example.remove('Hello')
print(set_example)
