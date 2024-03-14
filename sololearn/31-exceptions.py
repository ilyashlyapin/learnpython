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

