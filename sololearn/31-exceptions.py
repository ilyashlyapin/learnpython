# You have already seen exceptions in previous code. 
# They occur when something goes wrong, 
# due to incorrect code or input. When an exception occurs, the program immediately stops.
# The following code produces the ZeroDivisionError exception by trying to divide 7 by 0: 
# num1 = 7
# num2 = 0
# print(num1/num2)

# An exception is an event, which occurs 
# during the execution of a program that disrupts 
# the normal flow of the program.
# Different exceptions are raised for different reasons. 
# Common exceptions:
# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly; 
# TypeError: a function is called on a value 
# of an inappropriate type;
# ValueError: a function is called on a value 
# of the correct type, but with an inappropriate value.

# When an exception occurs, the program stops executing.
# To handle exceptions, and to call code when 
# an exception occurs, you can use a try/except statement.
# The try block contains code that might throw an exception. 
# If that exception occurs, the code in the try block 
# stops being executed, and the code in the except block is run.
# If no error occurs, the code in the except block doesn't run.

try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")


# A try statement can have multiple different except blocks 
# to handle different exceptions.
# Multiple exceptions can also be put 
# into a single except block using parentheses, 
# to have the except block handle all of them.

try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")

# An except statement without any exception specified 
# will catch all errors. These should be used sparingly, 
# as they can catch unexpected errors 
# and hide programming mistakes.
   
try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")
   
# Problem: An ATM machine takes the amount 
# to be withdrawn as input and calls the corresponding 
# withdrawal method.
# In case the input is not a number, 
# the machine should output "Please enter a number".
# Use exception handling to take a number as input, 
# call the withdraw() method with the input as its argument,
# and output "Please enter a number", 
# in case the input is not a number.
   
def withdraw(amount):
   print(str(amount) + " withdrawn!")

#your code goes here
n=input()
try:
   int(n)
   withdraw(n)
except:
   print("Please enter a number")

# After a try/except statement, a finally block can follow. 
# It will execute after the try/except block, no matter if 
# an exception occurred or not.

try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

# The else statement can also be used with try/except 
  # statements. 
# In this case, the code within it is only executed
   # if no error occurs in the try statement.

try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)

# You can throw (or raise) exceptions 
# when some condition occurs. 
# For example, when you take user input 
# that needs to be in a specific format, 
# you can throw an exception 
# when it does not meet the requirements.
# This is done using the raise statement.

num = 102
if num > 100:
  raise ValueError

# Exceptions can be raised with arguments 
# that give detail about them.

name = "123"
raise NameError("Invalid name!")

# This makes it easier for other developers 
# to understand why you raised the exception.

# You are making a program to post tweets. 
# Each tweet must not exceed 42 characters.
# Complete the program to raise an exception,
# in case the length of the tweet is more than 42 characters.

tweet = input()

try:
    #your code goes here
    if len(tweet) > 42:
        raise Exception()
except:
    print("Error")
else:
    print("Posted")



