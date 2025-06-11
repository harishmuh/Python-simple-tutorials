# =======================
# Functions
# =======================

# A block of organized code
# that can accept input and produce output
# and can be used repeatedly.

# ============================
# Regular function
# def function_name():
#     block of code

def add(number1, number2):
    return number1 + number2

print(add(2, 5))
print(add(100, 200))

# ============================
# Function without input (parameters) and without output (return)

def greetings():
    print('Good morning!')

# Calling the function
greetings()

# Task: Create a function named menu that will display
# the main menu:
# 1. Check quota
# 2. Top-up balance
# 3. Exit

def menu():
    print('''Main Menu
1. Check quota
2. Top-up balance
3. Exit''')

menu()

# =======================================
# Function with input (parameters) but without output

def introduction(name, location, age):
    print(f'Hello, my name is {name}')
    print(f'I live in {location}')
    print(f'I am {age} years old')

introduction('Imam', 'Binjai', 23)  # Must be in order

# If order is not desired
introduction(age=23, name='Ika', location='Bandung')

# Task: Create a function named oscar with parameters
# actor name, movie title, and year.
# The output should be:
# 'The Best Actor winner in 2016 was Leonardo DiCaprio for the movie The Revenant'

def oscar(name, movie, year):
    '''
    This function displays the Oscar-winning actor based on the year and movie title.

    Args:
        name (str): Actor's name
        movie (str): Movie acted in
        year (int): Year of the Oscar award

    Returns:
        None
    '''
    print(f'The Best Actor winner in {year} was {name} for the movie {movie}')

# oscar('Leonardo DiCaprio', 'The Revenant', 2016)
# oscar('Cillian Murphy', 'Oppenheimer', 2023)

# ============================
# Function with input (parameters) and with output (return)

# def add(number1, number2):  # With input and output
#     result = number1 + number2
#     return result  # Using return to produce a value
#                    # Allows mathematical operations

# def add_print(number1, number2):
#     result = number1 + number2
#     print(result)

# print(add(3, 5))   # Output is an integer: 8
# print(add_print(3, 5))  # Output is a print statement: 8

# print(add(3, 5) - 3)  
# print(add_print(3, 5) - 3)  # Error: NoneType cannot be used in arithmetic operations

# Task: Create a function with parameters number1 and number2 that returns four values:
# 1. Sum
# 2. Difference
# 3. Product
# 4. Division result

def math_operations(number1, number2):
    sum_result = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    division = number1 / number2 
    return sum_result, difference, product, division

# Using unpacking
sum_result, difference, product, division = math_operations(10, 2)
print('The division result is', division)

# ==============================================================
# Default Parameters
# If we don’t provide arguments when the function is called,
# The function already has default values for those parameters.

# def greetings(name='Secret', age=0, location='Indonesia'):
#     print(f'Hello, my name is {name}, I am {age} years old, and I live in {location}')

# greetings('Mazaya', 22, 'Bandung')     # All arguments provided
# greetings('Ridwan', 24)                # Only name and age provided
# greetings('Banu')                      # Only name provided
# greetings(age=25)                      # Only age provided (by keyword)

# def greetings(name='Secret', age=0, location='Indonesia'):
#     if name == 'Secret':
#         print('I do not want to reveal my name')
#     elif age == 0:
#         print(f'My name is {name}. I do not want to disclose my age')
#     elif location == 'Indonesia':
#         print(f'My name is {name}. My location is unknown')
#     else:
#         print(f'Hello, my name is {name}, I am {age} years old, and I’m from {location}')

# greetings('Iki', 23, 'Bandung')
# greetings(age=20, location='Bandung')
# greetings('Aga')
# greetings('Arya', 19)

# =================================================================
'''
Global Variables
-A variable defined outside a function.
-Its value is valid as long as the program runs.
-Can be accessed both inside and outside of functions.
'''

# case a
# x = 100  # This is a global variable

# def get_result():
#     print(x)  # Accessing global variable
#     a = 200   # Local variable
#     return a + 5

# get_result()
# print(get_result())  # Prints result using both global and local variables
# print(type(get_result()))
# print(a)  # Error: 'a' is local and cannot be accessed outside the function

# case b
# x = 100  # Global variable

# def get_result():
#     a = x + 20  # Using global x, 'a' is local
#     return a

# print('case b', get_result())

# case c
# x = 100  # Global variable

# def get_result():
#     a = x + 20       # x is used before it’s redefined locally → causes an error
#     x = 10           # Local x is defined here
#     return a

# # print(get_result())  # Error: local x is referenced before assignment

# Case d
# x = 100  # Global variable

# def get_result():
#     a = x + 20       # x is used before it’s redefined locally → causes an error
#     x = 10           # Local x is defined here
#     return a

# # print(get_result())  # Error: local x is referenced before assignment

# Case e
# x = 100  # Global variable

# def get_result():
#     x = 20
#     x = x + 20     # Local x
#     return x

# print(get_result())     
# print(x)  # Still prints 100 (global x is unchanged)

# ====================================
# Alternative (using global keyword)
# x = 100  # Global variable

# def get_result():
#     global x      # Use the global x
#     x = x + 20    # Modify the global x
#     return x

# print(get_result())  # Result is 120
# print(x)             # Now x = 120

# ====================================
# Callback Function
# A function that takes another function as an argument
# def calculator(operator, num1, num2):
#     result = operator(num1, num2)
#     return result

# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1 - num2

# def multiply(num1, num2):
#     return num1 * num2

# def divide(num1, num2):
#     return num1 / num2

# print(calculator(add, 2, 5))
# print(calculator(multiply, 4, 6))

# =====================================
# Calling Other Functions (Call Stack)
# A function that uses another function inside it.

# def area(length, width):
#     return length * width

# def volume(length, width, height):
#     return area(length, width) * height

# print(area(2, 5))
# print(volume(2, 5, 4))

# def display(answer):
#     print(f'The answer is {answer}')

# def print_volume(length, width, height):
#     answer = area(length, width) * height
#     display(answer)

# print_volume(2, 4, 5)



