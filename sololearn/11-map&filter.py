## to remember
# Python allows us to create functions on-the-fly, provided that they are created using lambda syntax. 

def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)

print((lambda x: x**2 + 5*x + 4) (-4))

# The function map takes a function and an iterable as arguments, 
# and returns a new iterable with the function applied to each argument.

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

# same result can be achived via lambda function

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

#To convert the result into a list, we used list explicitly.

# Task: Given a list of salaries, you need to take the bonus everybody is getting as input and increase all the salaries by that amount.
# Output the resulting list. 
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())
salaries = list(map(lambda x: x+bonus, salaries))

print(salaries)

