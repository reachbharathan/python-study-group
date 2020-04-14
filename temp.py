greeting = "good morning"

print(greeting)
def greet():
  print("hello")

def changeGreeting():
  greeting = "good afternoon"
  print(greeting)

class Dog:
  name=  "bharath"
  colour= "Black"
  def changeColour(self,colour):
    self.colour = colour

# greet()
changeGreeting()
print(greeting)

dog = Dog()
print(dog.colour)
dog.changeColour("red")
print(dog.colour)







