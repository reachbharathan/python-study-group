# Parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

# Parent class


class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

    def specialMethod(self, speed):
    return "%s runs %s" % (self.name, speed)

    def myNewDescription(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name, self.color, self.kind, self.price)
        return desc_str


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# Create instances of dogs
# my_dogs contains list of objects of Type Dogs class
my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

##
##
bulldog = Bulldog("Tom", 6)
# bulldog = my_dogs[0];
bulldog.tail = "long"  # does it allow to create a variable dynamically
print(bulldog)
print(bulldog.name)
print(bulldog.age)
print(bulldog.tail)
###
# Instantiate the Pets class
my_pets = Pets(my_dogs)

print(my_pets.dogs[0])  # [{name, age},{name, age},{name, age}]
print(my_pets.dogs[0].tail)


# # Output
# print("I have {} dogs.".format(len(my_pets.dogs)))
# for dog in my_pets.dogs:
#     dog.eat()
#     print("{} is {}.".format(dog.name, dog.age))

# print("And they're all {}s, of course.".format(dog.species))

# are_my_dogs_hungry = False
# for dog in my_pets.dogs:
#     if dog.is_hungry:
#         are_my_dogs_hungry = True

# if are_my_dogs_hungry:
#     print("My dogs are hungry.")
# else:
#     print("My dogs are not hungry.")
