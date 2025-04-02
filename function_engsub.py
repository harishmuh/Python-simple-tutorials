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

oscar('Leonardo DiCaprio', 'The Revenant', 2016)
oscar('Cillian Murphy', 'Oppenheimer', 2023)

# ============================
# Function with input (parameters) and with output (return)

def add(number1, number2):  # With input and output
    result = number1 + number2
    return result  # Using return to produce a value
                   # Allows mathematical operations

def add_print(number1, number2):
    result = number1 + number2
    print(result)

print(add(3, 5))   # Output is an integer: 8
print(add_print(3, 5))  # Output is a print statement: 8

print(add(3, 5) - 3)  
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

# =========
# Default parameters

# If no argument is provided when calling the function,
# the function uses a default value for that parameter.

def greetings(name='Unknown', age=0, location='Indonesia'):
    print(f'Hello, my name is {name}, I am {age} years old, and I live in {location}')

greetings('Mazaya', 22, 'Bandung')
greetings('Ridwan', 24)
greetings('Banu')
greetings(age=25)

def greetings(name='Unknown', age=0, location='Indonesia'):
    if name == 'Unknown':
        print('I do not wish to reveal my name')
    elif age == 0:
        print(f'My name is {name}. I do not want to disclose my age')
    elif location == 'Indonesia':
        print(f'My
