'''
Decision Structures
if-else statements
-   also known as branching strucutres
-   allow program to decide on course of action
        - based on wether a certin condition is true or false
-   form:
        if condition:
            indented block of statement
        else:
            indent block of statements
'''
# from multiprocessing import Condition

# grade = 98
# condition = grade >= 90
# if condition:
#     print("your grade is A")
# else:
#     print("Your grade is not A")

#  Examples 1: Program finds large of two numbers input by user.

# Determine the larger of the two numbers.
#  Obtain the two numbers from the user.
# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# #  Determine and display the larger value.
# if num1 > num2:
#     largeValue = num1 # execute this statment if the condition is true
# else:
#     largeValue = num2 # execute this statement if the condition is false
# print("The larger value is", str(largeValue) + ".")
'''
is-else Statement
Example 2: if-else statment in program has relational operators in its condition.
'''
# ## A quiz.
# #  Obtain answer to question.
# answer = eval(input("how many gallons does a ten-gallon hat hold? "))
# # Evaluate answer.
# if (0.5 <= answer <= 1):
#     print("good, ", end="")
# else:
#     print("No, ", end="")
# print("it holds about 3/4 of a gallon.")
# # How many gallons does a ten-gallon hat hold? = 10
# # No, it holds about 3/4 of a gallon.

'''
The else part of an if-else statement can be omitted
when the conditions is false
    - Execution continues with line after if statement block
Example 3: Program contains two if statments
'''
# ## find the largest of three numbers.
# #  Input the three numbers.
# firstNumber = eval(input("Enter first number: "))
# secondNumber = eval(input("Enter second number: "))
# thirdNumber = eval(input("Enter third number: "))
# # Determine and display the largest value.
# max = firstNumber
# if secondNumber > max:
#     max = secondNumber
# if thirdNumber > max:
#     max = thirdNumber
# print("The largest number is", str(max) + ".")

# numbers = [1, 28, 90]
# print(max(numbers))

# numbers = []
# firstNumber = eval(input("Enter first number: "))
# secondNumber = eval(input("Enter second number: "))
# thirdNumber = eval(input("Enter third number: "))
# numbers.append(firstNumber)
# numbers.append(secondNumber)
# numbers.append(thirdNumber)

# print("The largest number is", + str(max(numbers)) + ",")

'''
Nested if-else Statements
    - Indented blocks of if-else and if statments can contain other if-else and statments
        - The if-else statments are said to be nested
    - Consider the taks of interpreting a beacon
        - The color of the beacon light atop Boston's old John Hancock forecasts the weather
### Steady blue, clear view; Flashing blue, clouds due; Steady red, rain ahead; Flashing red, snow instead.

Example 4: Program request a color (Blue or Read) and a mode (Steady or Flashing) as input
    - Then display the weather forcase
'''

# ##Interpret weather beacon.
# #  Obtain color and mode.
# color = input("Enter a color (BLUE or RED): ")
# mode = input("Enter a mode (STEADY or FLASHING): ")
# color = color.upper()
# mode = mode.upper()
# #  Analyze responses and display weather forecast.
# result = ""
# if color == "BLUE":
#     if mode == "STEADY":
#         result = "Clear View"
#     else:   #mode is FLASHING
#         result = "Clouds due"
# else: #color is READ
#     if mode == "STEADY":
#             result = "Rain Ahead."
#     else: # mode is FLASHING
#             result = "Snow Instead."
# print("The weather forecast is", result)   

"""Example 5"""

# ## Evaluate profit
# # Obtain input from user.
# costs = eval (input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))
# # Determin and display profit or loss
# if costs == revenue:
#     result = "Break even."
# else:
#     if costs < revenue:
#         profit = revenue - costs
#         result = "Profit is ${0:,.2f}".format(profit)
#     else:
#         loss = costs - revenue
#         result = "Loss is ${0:,.2f}.".format(loss)
# print(result)
'''Simplified'''
# costs = eval (input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     print("break Even.")
# result = "is ${0:,.2f}".format(revenue - costs)
# if (revenue - costs) < 0:
#     print("Loss " + result)
# print("Profit " + result)

"""The elif Clause""" '''Example 6'''

# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# if num1 > num2:
#     print("The larger value is", str(num1) + ",")
# elif num2 > num1:
#     print("The larger value is", str(num2) + ",")
# else:
#     print("the two values are equal.")

'''Example 7'''
# DO AT HOME!!!

'''Example 8'''

# gpa = eval(input("Enter your gps: "))
# if gpa >= 3.9:
#     honors = " summa cum laude."
# elif gpa >= 3.6:
#     honors = " magna cum laude."
# elif gpa >= 3.3:
#     honors = " cum laude."
# else:
#     honors = "."
# print("Your graduation" + honors)

'''Example 9'''

# num1 = input("Enter fist number: ")
# num2 = input("Enter second number: ")
# if num1.isdigit() and num2.isdigit():
#     print("The sum is", str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number.")
#     print("The first entry was not a proper number.")
# print("The second entry was not a proper number.")

'''Example 10'''

if 7:
    print("A nonzero numer is true.")
else:
    print("The number zero is false.")
if []:
    print("A nonempty list is true.")
else:
    print("An empty list is fasle.")
if ["spam"]:
    print("A nonempty list is true.")
else:
    print("The empty list is false.")

