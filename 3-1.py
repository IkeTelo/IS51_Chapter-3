"Relation and Logical Operatiors"
# Condition is exoression 
#   - Involving relational operators (such as < and > =)
#   - Logical operatiors (i.e. and, or, and not)
#   - Evaluates to either True or False
#  Conditions used to make decicions"
#   - control loops
#   - choose between options

"ASCII Values"
# ASCII values determin order used to compare strings with relational operators
# Associated with keyboard letters, charachters, numerals
#   - ASCII values are numbers ranging from 32 to 126
#  A few ASCII values
# 32 = space, 33 = !, 34 = ", 35 = #, 48 = 0, 49 = 1, 57 = 9, 65 = A, 66 = B, 90 = Z, 97 = a, 98 = b, 122 = z, 123 = (, 125 = ), 126 = ~

"""
Relational Operator
<, <=, >, >=, !=, ==, in, not in;
    (less than, less or equal than, greater than, greater or equal than, not equal to, equal to)
Logical Operator
and, or, not
"""
#  Relational operatior less than (<) can be applied to
#   - numbers, strings, and other objects
#  for strings, the ASCII table determines order of charachters
# in = substring of, and no in = not a substring of

#  some rules
#   - an int can be compared to a float, otherwise values of diffrent types cannot be compared, relational operatora can be applied to list or tuples

# true_or_false = "b" > "a"; #True
# true_or_false = "z" < "!"; #True
# true_or_false = "z" < "!" and "b" > "a"; #False
# true_or_false = "z" < "!" or "b" > "c"; #True


# C = "abc"
# C < "good" + "d"
# true_or_false = C < "good" + "d"

# true_or_false = 3 in [3, 8]
# true_or_false = "b" > "a"
# true_or_false = "z" < "!"
# print("true_or_fasle", true_or_false)

"""
Some Rules;
    - An int can be compared to a float
    - Otherwise, values of diffrent types cannot be compared
    - Relational operators can be applied to lists or tuples
"""
# true_or_false = [3, 5] < [3, 7]
# print(true_or_false)
# true_or_false = [3, 5] < [3, 5, 6]
# print(true_or_false)
# true_or_false = [3, 5, 7] < [3, 7, 2]
# print(true_or_false)
# true_or_false = [7, "three", 5] < [7, "two, 2"]
# print(true_or_false)
# true_or_false = "!" > "0"
# print(true_or_false)

# EXAMPLE 1:

# true_or_false = 1 <= 1
# true_or_false = 1 < 1
# true_or_false = "car" < "cat"
# true_or_false = "Dog" < "dog"
# true_or_false = "fun" in "refunded"
# print(true_or_false)

#  EXAMPLE 2:
# a = 1
# b = 2
# true_or_false = (a + b) < (2 * a)
# true_or_false = (len(c) - b) == (a/2)
# true_or_false = c < ("good" + d)
# print("true_or_false is ", true_or_false)

"""
Sorting the item in a list
    - Items in a list of items having same data type can be ordered with the sort method
"""

# list1 = [6, 4, -5, 3.5]
# print(list1)
# list1.sort()
# print(list1)

# list2 = ["ha", "hi", "b", "7"]
# print(list2)
# list2.sort()
# print(list2)


# EXAMPLE 4: items in a complicated list of strings.

# list1 = [chr(177), "cat", "car", "Dog", "dog", "8-ball", "5" + chr(162)]
# list1.sort()
# print(list1)
# [RUN] = ['5¢', '8-ball', 'Dog', 'car', 'cat', 'dog', '±']

# EXAMPLE 5: Items in a list of tuple.

# monarchs = [("George", 5), ("Elizabeth", 2), ("George", 6), ("Elizabeth", 1)]
# monarchs.sort()
# print(monarchs)
# [RUN] = [('Elizabeth', 1), ('Elizabeth', 2), ('George', 5), ('George', 6)]


"""
Logical Operators
    - Enables combining multiple relational operators
    - Logical operators are the reserved words and, or, and not
    - Conditions that ue these operatios are called compound conditions
Given: cond1 and cond are conditions
    - cond1 and cond2 true only if both conditons are true
    - cond1 or cond2 true if either or both conditions are true
    - not cond1 is false if condition is true, true if the condition is false
"""
#  EXAMPLE 6:
# n = 4
# answ = "Y"
# true_or_false = (2 < n)and(n < 6)
# print(true_or_false)
# true_or_false = (2 < n)or(n == 6)
# print(true_or_false)
# true_or_false = not(n < 6)
# print(true_or_false)
# true_or_false = (answ == "Y")or(answ == "y")
# print(true_or_false)
# true_or_false = (answ == "Y")and(answ == "y")
# print(true_or_false)
# true_or_false = not(answ == "y")
# print(true_or_false)
# true_or_false = ((2 < n)and(n == 5 + 1))or(answ == "No")
# print(true_or_false)
# true_or_false = ((n == 2)and(n == 7))or(answ == "y")
# print(true_or_false)
# true_or_false = (n == 2)and(n == 7)or(answ == "Y")
# print(true_or_false)

"""
Short-Circuit Evaluation
    - Consider the condition cond1 and cond2
        - If python evaluates cond1 as false, it does not bother to check cond2
    - Similarly with cond1 and cond2
        If Python finds cond1 true, it does not bother to check further
    - Think why this feature helps for;
    (number ! = 0) and (m == (n / number))
"""
"""
The bool Data Type
    - Object True and False are said to have Boolean data type
        - Of data type bool
    - What do these lines disply? = True, False
"""
# x = 2
# y = 3
# var = x < y
# print(var)
# x = 5
# print((3 +x) < 7)

"""
Methods that Return Boolean Vales
    - Given: strings str1 and str2
        - str1.startswith(str2)
        - str1.endswith(str2)
    - For determining the type of an item
        - isinstance(item, dataType)
    - Methods that return either True or False.
    str.isdigit() = all of str1's charachters are digits
    str1.isalpha() = all of str1's charachters are letters of the alphabet.
    str.isalnum() = all of str1's characters are letter of the alphabet or digits
    str1.islower() = str1 has at least 1 alphabetic charachter and all of its alphabetic charachters are lowercase
    srt1.isupper() = str1 has at least 1 alphabetic charachter and all of its alphabetic charachters are uppercase.
    str1.ispace() = str1 contains only whitespace charachters
"""

"""
Simplifying Condtions
    - Lists or tuples can sometimes be used to simplify long compound conditions
    """
# (state == "MD") or (state == "VA") or state == "WV") or (state == "DE")
#    # can be replaced with the condition
# state in [ "MD", "VA", "WV", "DE"]
