# Magic methods are special methods which have double underscores 
# at the beginning and end of their names. 
# They are also known as dunders. 
# So far, the only one we have encountered is __init__, but there are several others. 
# They are used to create functionality that can't be represented as a normal method. 
# One common use of them is operator overloading. 
# This means defining operators for custom classes 
# that allow operators such as + and * to be used on them.
# An example magic method is __add__ for +.
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

# The __add__ method allows for the definition 
# of a custom behavior for the + operator in our class.
# As you can see, it adds the corresponding attributes 
# of the objects and returns a new object, containing the result.
# Once it's defined, we can add two objects of the class together.

# More magic methods for common operators:
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |
# The expression x + y is translated into x.__add__(y). 
# However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called. 
# There are equivalent r methods for all magic methods just mentioned.

class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])
  
spam = SpecialString("spam")
hello = SpecialString("Hello world!!!")
print(spam / hello)

# In the example above, we defined the division operation 
# for our class SpecialString.

# Python also provides magic methods for comparisons.
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=
# If __ne__ is not implemented, it returns the opposite of __eq__. 
# There are no other relationships between the other operators.

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

# you can define any custom behavior 
# for the overloaded operators.

# There are several magic methods for making classes act 
# like containers.
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g., in for loops)
# __contains__ for in
# There are many other magic methods that we won't cover here, 
# such as __call__ for calling objects as functions, 
# and __int__, __str__, and the like, for converting objects 
# to built-in types.

import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2]) 

# We are improving our drawing application.
# Our application needs to support adding and comparing two Shape objects. 
# Add the corresponding methods to enable addition + and comparison using the greater than > operator for the Shape class.
# The addition should return a new object with the sum of the widths and heights of the operands, while the comparison should return the result of comparing the areas of the objects.

class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height

    #your code goes here
    def __add__(self, other):
        return Shape(self.width + other.width, 
        self.height + other.height)

    def __gt__(self, other):
        return self.area() > other.area()

w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)

# The given code creates two Shape objects from uxser input, 
# outputs the arexa() of their addition and compares them.   