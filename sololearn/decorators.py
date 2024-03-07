# Decorators provide a way to modify functions using other functions. 
# This is ideal when you need to extend the functionality of functions 
# that you don't want to modify.

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

# In our previous example, we decorated our function 
# by replacing the variable containing the function with a wrapped version.

def print_text():
  print("Hello world!")

print_text = decor(print_text)

# This pattern can be used at any time, to wrap any function.
# Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
# If we are defining a function we can "decorate" it with the @ symbol like:
@decor
def print_text():
  print("Hello world!")

# task You are working on an invoicing system.
# The system has an already defined invoice() function, 
# which takes the invoice number as argument and outputs it.
# You need to add a decorator for the invoice() function,
# that will print the invoice in the following format:
# Sample Input
# 42
# Sample Output
# ***
# INVOICE #42
# ***
# END OF PAGE  
  
def decor(func):
    def wrap(num):
        print("***")
        func(num)
        print("***")
        print("END OF PAGE")
    return wrap

@decor
def invoice(num):
    print("INVOICE #" +num)


invoice(input());

