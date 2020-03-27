class Character:

    def __init__(self, name, initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []

    def __str__(self):
       s = "Name: " + self.name
       s += " Health: " + str(self.health)
       s += " Inventory: " + str(self.inventory)
       return s


    def grab(self, item):
       self.inventory.append(item)

    def get_health(self):
       return self.health


def example():
    lin = Character("Lin", 100)
    print(str(lin))
    lin.grab("pencil")
    lin.grab("paper")
    print(str(lin))
    print("Health: ", lin.get_health())

example() 

# Object oriented programming is a programming paradigm that uses objects to solve the real world problems. We use class to define new types of objects. A class has three important concepts: encapsulation, inheritance and polimorphism.

# A method is a special function that is defined inside a class.

# __init__() is a special method that initializes an object. init method has three arguments: self, name and initial_health. self is a reference that points to a new object.

# __str__() is string method that return an object string information.

# grab and get_health are methods that model the object behaviors.
 
# Character() is a construction function 


