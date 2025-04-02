#================================
# Looping Statements
#================================
# Purpose: Execute a block of code repeatedly

# Displaying 3 identical lines manually
# print('I am learning Data Science')
# print('I am learning Data Science')
# print('I am learning Data Science')

# Using a loop
# for i in range(5):  # Print 5 times
#     print('I am learning Data Science')

# ======================
# While Loop
# ======================
# As long as the condition is met,
# the loop will continue to run.
# The loop will stop when the condition becomes False.

# Infinite loop
# Why? The program runs indefinitely because the condition is always True. 
# ---> MUST BE AVOIDED

# x = 1
# while x <= 5:  # This will run indefinitely because x = 1 is always True  # MUST BE AVOIDED
#     print('I am learning Data Science')  
#     # To stop: Press Ctrl + C

# Example of a while loop 1
# x = 1
# while x <= 5:
#     print('I am learning Data Science')
#     x = x + 1

# Example of a while loop 2 
# number = 1
# while number <= 3:
#     print(f'Number: {number}')
#     number += 1

# Example of a while loop 3  # Output: 2,3,4
# number = 1
# while number <= 3:
#     number += 1
#     print(f'Number: {number}')

# =========================================
# WHILE ELSE Statement
# =========================================
# number = 0
# while number < 3:
#     print(f'I am learning Data Science, session - {number + 1}')
#     number = number + 1
# else:
#     print('I want to take a break')

'''
# Task: Using a loop
# Display even numbers up to 14
'''

# # Method 1
# number = 0
# while number < 15:
#     if number % 2 == 0:
#         print(number, end=' ')
#     number = number + 1
# print()

# Method 2
# number = 2
# while number < 15:
#     print(number, end=' ')
#     number = number + 2

# ==================
# For Loop
# ==================
# The loop will continue to run as long as there are items or elements
# inside a data collection or iterable.

# =====================
# Looping through a List
# =====================

# Example 1
# for i in [2,4,6,8]:
#     print(f'Number in the list: {i}')

# Example 2
# numbers_list = [2,4,6,7,9]
# for value in numbers_list:
#     print(value)

# Example 3
# numbers_list = [1,2,3,4,5]
# for value in numbers_list[1:4]:  # From index 1 to index before 4
#     print(f'Value: {value}')

# Example 4
# numbers_list = [3, 6, 9, 12, 15]
# for value in numbers_list:
#     print('I am learning')  # Will print 5 times, equal to the number of items in the list

# Example 4.5
# numbers_list = [3, 6, 9, 12, 15]
# for value in numbers_list:
#     print(f'I am learning DS for {value} hours')  # Prints 5 times based on list size

# Example 5
# items_list = ['book', 'bag', 'pencil']
# for item in items_list:
#     print(f'I am carrying a {item}')

# Example 6
# Summing all numbers in a list using a for loop
# numbers_list = [2, 5, 7, 9, 14, 23, 35, 61, 78, 100]

# total = 0
# for number in numbers_list:
#     total += number  # Equivalent to total = total + number

# print(f'The total is: {total}') 

#========================================================
# Looping over a Range (start, stop, step)
#========================================================

# By default, the start value is 0, step size is 1,
# stop value is not included.

# print('range(5)')
# for value in range(5):  # range(stop): start=0, stop=5, step=1
#     print(value)

# print('range(2,5)')
# for value in range(2,5):  # range(start, stop): start=2, stop=5, step=1 
#     print(value)

# print('range(2,10,3)')
# for value in range(2,10,3):  # range(start, stop, step): start=2, stop=10, step=3 
#     print(value)

# print('range(3,0,-1)')
# for value in range(3,0,-1):  # range(start, stop, step): start=3, stop=0, step=-1
#     print(value)

'''
Task: Using a for loop, display the following output:
Output:
list = [1, 4, 9, 16, 25]
'''
# numbers_list = [1, 4, 9, 16, 25]
# for i in range(1,6):
#     print(i**2, end=' ')

'''
# Task 2: Using a for loop, display the following output:
# Output:
# Number 1 is not a multiple of 3
# Number 2 is not a multiple of 3
# Number 3 is a multiple of 3
# Number 4 is not a multiple of 3
# Number 5 is not a multiple of 3
# Number 6 is a multiple of 3
'''
# for i in range(1,7):
#     if i % 3 == 0:
#         print(f'Number {i} is a multiple of 3')
#     else:
#         print(f'Number {i} is not a multiple of 3')

'''
# Task 3: Create a for loop using range based on the following list:
# fruit_list = ['orange', 'apple', 'mango'] 
# Output: 
# Fruit number 1 is orange
# Fruit number 2 is apple
# Fruit number 3 is mango
'''
# fruit_list = ['orange', 'apple', 'mango']
# for i in range(len(fruit_list)):
#     print(f'Fruit number {i+1} is {fruit_list[i]}')

# ========================
# Looping through a Dictionary
# ========================

car_brands = {
    'toyota': 'innova',
    'honda': 'civic',
    'daihatsu' : 'sigra'
}

# Display only the keys
# for brand in car_brands:
#     print(brand) 

# Display only the values
# for model in car_brands.values():
#     print(model)

# Display both keys and values
# for brand, model in car_brands.items():
#     print(f'Brand {brand} produces the {model} model')

'''
# Task: Using a for loop on a dictionary, display:
# Output:
# Brand toyota produces the innova model
# Brand honda produces the civic model
# Brand daihatsu produces the sigra model
'''
# for brand, model in car_brands.items():
#     print(f'Brand {brand} produces the {model} model')

# ===================
# Nested Loops
# ===================

# Nested loops: a loop inside another loop.
# The inner loop executes fully before moving to the outer loop.

# for bite in range(1,4):
#     print(f'This is bite number {bite}')
#     for dish in ['rice', 'beef stew', 'jackfruit leaves', 'chili sauce']:
#         print(f'The dish is {dish}')
