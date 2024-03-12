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

# Recursion can also be indirect. 
# One function can call a second, which calls the first, 
# which calls the second, and so on. This can occur with any number of functions.

def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)


print(is_odd(17))
print(is_even(23))

# The given code defines a recursive function convert(), which needs to convert its argument from decimal to binary.

# However, the code has an error. 

# Fix the code by adding the base case for the recursion, then take a number from user input and call the convert() function, to output the result.

def convert(num): 
   if num ==0:
      return 0
   else: 
      return (num % 2 + 10 * convert(num // 2)) 

intvalue = int(input())

print(convert(intvalue))

