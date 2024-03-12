# Python allows you to have functions with varying numbers of arguments.

# Using *args as a function parameter enables you to pass 
# an arbitrary number of arguments to that function. 
# The arguments are then accessible as the tuple args in the body of the function.

def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)

#The parameter *args must come after the named parameters to a function.
# The name args is just a convention; you can choose to use another.

# **kwargs (standing for keyword arguments) allows you to handle named arguments 
# that you have not defined in advance.
# The keyword arguments return a dictionary in which the keys are the argument names, 
# and the values are the argument values.

def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

# a and b are the names of the arguments that we passed to the function call.

# The given code defined a function called my_min(), 
# which takes two arguments and returns the smaller one.

# You need to improve the function, so that it can take any number of variables, 
# so that the function call works.

def my_min(x,y,*args):
    for i in args:
        if i < y:
            return i    
        else:
            return y

print(my_min(8, 13, 4, 42, 120, 7))

