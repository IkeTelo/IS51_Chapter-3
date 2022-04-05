'''The While Loop'''

'''Example 1'''
# i = 0 # i is used as an iterator as the varriable "i"
# while (i < 10):
#     i = i + 1
#     print("Hello World! " + str(i))

# i = 0 # i is used as an iterator as the varriable "i"
# while i < 10:
#     print("Hello World! " + str(i))
#     i =+ 1 # i = i + 1 (equals!) in C or C+ we can use i++ NOT on python


'''EXAM know the Flow Chart for Loop!'''

'''Example 2'''
# print("This program displays a famous movie quatation.")
# responses = ('1', '2', '3')
# response = '0'
# while response not in response:
#     response = input ("Enter 1, 2, or, 3: ")
#     if response == '1':
#         print("Plastics.")
#     elif response == '2':
#         print("Rosebud.")
#     elif response == '3':
#         print("That's all folks.")

# print("This program displays a famous movie quatation.")


# resps = ("1", "2", "3")
# resp = "0"

# while resp not in resps: # = to while "0" is not in ("1", "2", "3")
#     resp = input("Enter 1, 2, or, 3: ")
#     if resp == "1":
#         print("Plastic.")
#     elif resp == "2":
#         print("Rosebud.")
#     elif resp == "3":
#         print("That's all folks.")

'''Example 3!'''
# count = 0
# total = 0
# print("(Enter -1 to terminate entering numbers.)")
# num = eval(input("Enter a nonnegitive number: "))
# min = num
# max = num
# while num != -1:
#     count += 1
#     total += num
#     if num < min:
#         min = num
#     if num > max:
#         max = num
#     num = eval (input("Enter a nonnegitive number: "))

# if count > 0:
#     print("Min: ", str(min))
#     print("Max: ", str(max))
#     print("Average: ", str(total / count))
# else:
#     print("No nonnegitive numbers were entered")

"How can we make this better?"
# count = 0
# numbers = []
# print("(Enter -1 to terminate entering numbers.)")
# num = eval(input("Enter a nonnegitive number: "))
# numbers.append(num)
# while num != -1:
#     count += 1
#     num = eval (input("Enter a nonnegitive number: "))
# if count > 0:
#     print("Min: ", str(min(numbers)))
#     print("Max: ", str(max(numbers)))
#     print("Average: ", str(sum(numbers) / count))
# else:
#     print("No nonnegitive numbers were entered")

# '''Example 4'''
# list1 = []
# print("(Enter -1 to terminate entering numbers.)")
# num = eval(input("Enter a nonnegative number: "))
# while num != -1:
#     list1.append(num)
#     num = eval(input("Enter a nonnegative: "))
# if len(list1) > 0:
#     list1.sort()
#     print("Minimun:", list1[0])
#     print("Maximun:", list1[-1])
#     print("Average:", sum(list1) / len(list1))
# else:
#     print("No nonnegative numbers were entered.")
'''Example 5'''
