# The class describes what the object will be, but is separate from the object itself. 
# In other words, a class can be described as an object's blueprint, description, or definition.
# You can use the same class as a blueprint for creating multiple different objects. 
# Classes are created using the keyword class and an indented block, 
# which contains class methods (which are functions). 
# Below is an example of a simple class and its objects.

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# Classes can have other methods defined to add functionality to them. 
# Remember, that all methods must have self as their first parameter.
# These methods are accessed using the same dot syntax as attributes.

class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

# You are making a video game! The given code declares a Player class, 
# with its attributes and an intro() method.
# Complete the code to take the name and level from user input, create a Player object with the corresponding values and call the intro() method of that object.
# Sample Input:
# Tony
# 12
# Sample Output:
# Tony (Level 12)

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

#your code goes here
name = input()
level = input()
p1 = Player(name, level)
p1.intro()


