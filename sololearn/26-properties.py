# Properties provide a way of customizing access 
# to instance attributes. 
# They are created by putting the property decorator 
# above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead. 
# One common use of a property 
# is to make an attribute read-only.

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    
  @property
  def pineapple_allowed(self):
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
# Properties can also be set by defining 
# setter/getter functions.
# The setter function sets the corresponding property's value.
# The getter gets the value.
# To define a setter, you need to use a decorator 
# of the same name as the property, followed by a dot and the setter keyword.
# The same applies to defining getter functions.

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

# We are improving our game and need to add an isAlive property, 
# which returns True if the lives count is greater than 0.
# Complete the code by adding the isAlive property.
# The code uses a while loop to hit the Player,
# until its lives count becomes 0, 
# using the isAlive property to make the condition.
class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
    
    #your code goes here
    @property
    def isAlive(self):
        if self._lives > 0:
            return True
            
p = Player("Cyberpunk77", int(input()))
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break
