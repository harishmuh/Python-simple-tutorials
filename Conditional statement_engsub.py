# ======================
# Conditional Statements
# ======================

# Boolean --> A data type that has values of either True or False
# print(True)
# print(False)

# ===========================
# Comparison Operators:

# print('5>3:', 5 > 3)  # greater than --> True
# print('5<3:', 5 < 3)  # less than --> False
# print('5>= 6:', 5 >= 6)  # greater than or equal to --> False
# print('5<= 5:', 5 <= 5)  # less than or equal to --> True
# print('5!= 5:', 5 != 5)  # not equal to --> False
# print('5== 5:', 5 == 5)  # equal to --> True
# print('Ridwan == ridwan:', 'Ridwan' == 'ridwan')  # False (case-sensitive)
# print('a < b:', 'a' < 'b')  # True (based on ASCII values)
# print('A > a:', 'A' > 'a')  # False (based on ASCII values)
# print('1 > a:', 1 > 'a')  # Error because int cannot be compared with str

########################################
# Logical Operators: and, or, not

# ======== and
# and --> All conditions must be True for the result to be True
# and --> Will be False if at least one condition is False

# print('True and True:', True and True)  # True
# print('True and False:', True and False)  # False
# print('False and False:', False and False)  # False

# ========= or
# or --> Will be True if at least one condition is True

# print('True or True:', True or True)  # True
# print('True or False:', True or False)  # True
# print('False or False:', False or False)  # False

# print('True and True and True:', True and True and True)  # True
# print('True and False and True:', True and False and True)  # False
# print('True or False or True:', True or False or True)  # True
# print('False or False or False:', False or False or False)  # False
# print('False or False and True:', False or False and True)  # False

# ========== Not
# Returns the opposite value

# print('not True', not True)  # False
# print('not False', not False)  # True

# print(5 < 3 and 7 > 8)  # False

# a = 5
# b = 'apple'

# print(a == 5 or b != 'apple')  # True

# =================================
# Conditional Statements
# =================================

# Conditional Statement
# - The program will perform a task if a condition is met (evaluates to True)
# - Definition: A statement that involves a condition to determine which task will be executed
# - The task will only be executed if and only if the condition evaluates to True

# Analogy:
# If I am hungry, then I eat
# If I am thirsty, then I drink

# =====================
# IF Statement
# ====================

# ======================================================
# IF Statement
# If the condition is met (evaluates to True), the program executes the task
# If the condition is not met (evaluates to False), the program does not execute the command

# Example 1:
# if True:
#     print('The program will run')

# Example 2:
# if False:
#     print('The program will run')  # This will not run

# Example 3:
# age = 17

# if age >= 17:
#     print(f'Your age is {age} years. Your driving license application is accepted')
#     print('Please contact the nearest police station')

# print('Program ends')  # Not part of the if statement due to lack of indentation

# Example 4:
# score_1 = 10
# score_2 = 20

# if score_1 > 15 or score_2 > 15:  # False or True --> True
#     result = score_1 + score_2
#     print(result)  # 30

# Exercise:  
# An Indonesian citizen is eligible for a scholarship if their IELTS score is above 6.

# input_ielts = float(input('What is your IELTS score?'))  # Input is always a string, so cast to float

# if input_ielts > 6:
#     print('Your IELTS score:', input_ielts)
#     print('Congratulations, you have received a scholarship')

# ====================================================
# IF-ELSE Statement

# If the condition in IF is True, the IF statement runs
# If the condition in IF is False, the ELSE statement runs

# age = 15

# if age >= 17:
#     print(f'Your age is {age} years. Your driving license application is accepted')
#     print('Please contact the nearest police station')
# else:
#     print('You do not meet the age requirement')
#     print('Wait until you turn 17')

'''
Problem:
Create an application that asks a user for a number input.  
The application will then display the following output:
- "The number you entered is ODD" if the number is odd
- "The number you entered is EVEN" if the number is even
- "The number you entered is INVALID" if the number is less than or equal to 0
'''

# input_number = int(input('Enter a number: '))

# if input_number <= 0:
#     print('INVALID number')
# else:
#     if input_number % 2 == 0:
#         print('The number is EVEN')
#     else:
#         print('The number is ODD')

# ===========================================
# IF-ELIF-ELSE Statement

# - If the condition in IF is True, the IF statement runs
# - If the condition in IF is False, the ELIF condition is evaluated
# - If the ELIF condition is True, the ELIF statement runs
# - If the ELIF condition is False, the ELSE statement runs
# - Only one condition is executed

# Case 1:
# if True:
#     print('This is the IF statement')
# elif False:
#     print('This is the ELIF statement')
# else:
#     print('This is the ELSE statement')

'''
Problem:
If score is 90 or above, grade A  
If score is 80 - 89, grade B  
If score is 70 - 79, grade C  
If score is 60 - 69, grade D  
If score is below 60, grade E
'''

# score = float(input('Enter your score: '))

# if score < 0 or score > 100:
#     print('Invalid score')
# else:
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     elif score >= 60:
#         grade = 'D'
#     else:
#         grade = 'E'
#     print(f'Your score is {score}. You received grade {grade}')

'''
Exercise:
Create a "Rock-Paper-Scissors" program where:
- Input 1 means choosing "Rock"
- Input 2 means choosing "Scissors"
- Input 3 means choosing "Paper"
'''

# input_choice = int(input('Enter 1, 2, or 3: '))

# if input_choice not in [1, 2, 3]:
#     print('Invalid input')
# else:
#     if input_choice == 1:
#         print('You chose Rock')
#     elif input_choice == 2:
#         print('You chose Scissors')
#     elif input_choice == 3:
#         print('You chose Paper')
