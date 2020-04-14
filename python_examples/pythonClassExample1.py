# define the Vehicle class
class Car:
    name = "NewName"
    kind = ""
    color = ""
    price = 0

    def myNewDescription(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name, self.color, self.kind, self.price)
        return desc_str


# your code goes here
car1 = Car()
print(car1.name)
car1.name = "Maruthi"  # override the default value of class
car1.color = "red"
car1.kind = "famil car"
car1.price = 400000


car2 = Car()
print(car2.name)
car2.name = "Hundai"
car2.color = "White"
car2.kind = "SUV"
car2.price = 800000
print(car1.name)
print(car2.name)

# car2 = Vehicle()
# car2.name
# car2.color
# car2.kind
# car2.value


# # test code
# # print(car1.description())
# # print(car2.description())
