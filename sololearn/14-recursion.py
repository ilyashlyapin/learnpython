# Recursion is a very important concept in functional programming. 

# The fundamental part of recursion is self-reference -- functions calling themselves. 
# It is used to solve problems that can be broken up into easier sub-problems of the same type.

# A classic example of a function that is implemented recursively is the factorial function, 
# which finds the product of all positive integers below a specified number. 

# For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement this recursively, 
# notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!. 

# Furthermore, 1! = 1. This is known as the base case, 
# as it can be calculated without performing any more factorials. 

# Below is a recursive implementation of the factorial function.

def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)
    
print(factorial(5))