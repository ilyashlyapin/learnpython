# Generators are a type of iterable, like lists or tuples. 
# Unlike lists, they don't allow indexing with arbitrary indices, 
# but they can still be iterated through with for loops. 
# They can be created using functions and the yield statement.
def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1
    
for i in countdown():
  print(i)

# The yield statement is used to define a generator, 
# replacing the return of a function to provide a result to its caller 
# without destroying local variables. 

# Due to the fact that they yield one item at a time, 
# generators don't have the memory restrictions of lists. 
# In fact, they can be infinite!
  
def infinite_sevens():
  while True:
    yield 7
        
for i in infinite_sevens():
  print(i)

# In short, generators allow you to declare a function
# that behaves like an iterator, i.e. it can be used in a for loop.
# Finite generators can be converted into lists by passing them as arguments to the list function.

def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))

# Using generators results in improved performance, 
# which is the result of the lazy (on demand) generation of values, 
# which translates to lower memory usage. 
# Furthermore, we do not need to wait 
#  until all the elements have been generated before we start to use them.

# Finding prime numbers is a common coding interview task.
def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    #your code goes here
    for number in range(a,b):
        if isPrime(number):
            yield number
    
f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))

# test


