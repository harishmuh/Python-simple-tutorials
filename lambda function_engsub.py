# ======================
# Lambda Function
# ======================

# A small function without a name
# Can have parameters, but only one expression/statement
# Syntax --> lambda parameter: expression

# Regular function
def multiply(num1, num2):
    return num1 * num2

print(f'Regular Function: {multiply(3, 4)}')

# Lambda Function
multiply_lambda = lambda num1, num2: num1 * num2  # Parameters are num1 and num2

print(f'Lambda Function: {multiply_lambda(3, 4)}')

# Task: Create a function named square with a parameter "num" that returns its squared value
square_lambda = lambda num: num ** 2
print(f'Lambda Function Square: {square_lambda(3)}')

# Task 2: Create a lambda function that returns the first letter of a word
# where the parameter is "word"

get_initial = lambda word: word[0]
print(f'Lambda Function Get Initial: {get_initial("Awesome")}')

# Task: Create a lambda function where the parameter is a number
# The function should return whether the number is even or odd

# Option 1
even_odd_lambda = lambda num: 'Even' if num % 2 == 0 else 'Odd'
print(f'Even or Odd: {even_odd_lambda(24)}')

# =========================
# List Comprehension and Looping
# =========================

numbers = [1, 2, 3, 4, 5]

# Squaring numbers using list comprehension
squared_numbers = [num ** 2 for num in numbers]
print(f'Squared Numbers (List Comprehension): {squared_numbers}')

# Squaring numbers using a loop
squared_numbers_loop = []
for num in numbers:
    squared_numbers_loop.append(num ** 2)

print(f'Squared Numbers (Looping): {squared_numbers_loop}')

# =========================
# Map Function
# =========================

# The map function is commonly used to transform values in a collection of data
# Syntax --> map(function, iterable)

def square(num):
    return num ** 2

print('Map - Regular Function:', list(map(square, numbers)))
print('Map - Lambda Function:', list(map(lambda x: x ** 2, numbers)))

# Task: Cube each number in the list using map
print('Cubed Numbers (Map & Lambda):', list(map(lambda x: x ** 3, numbers)))

# =========================
# Filtering Lists
# =========================

# The filter function is used to select certain values from a collection
# Syntax --> filter(function, iterable)
# The number of items may be reduced, but the values themselves remain unchanged

# Task: Filter out only odd numbers from the list
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print('Filtered Odd Numbers:', odd_numbers)

# =========================
# Recursive Function
# =========================

# A recursive function is a function that calls itself

def countdown(num):
    print(num)
    num -= 1

    if num > 0:
        countdown(num)

countdown(5)
