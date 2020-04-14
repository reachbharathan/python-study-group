def greeting_morning(name):
  print_str = "Good morning " + name
  print(print_str)
  

def greeting_afternoon(name):
  print_str = "Good afternoon " + name
  print(print_str)

def greeting_evening(name):
  print_str = "Good evening " + name
  print(print_str)

def executeFunc(func, name):
    func(name)
    print("Have a lovely day" + name)

time = 2
if (time == 1):
  # greeting_morning("Bharath")
  executeFunc(greeting_morning,"Bharath")
elif (time == 2):
  # greeting_afternoon("Bharath")
  executeFunc(greeting_afternoon,"Bharath")
elif (time == 3):
  # greeting_evening("Bharath")
  executeFunc(greeting_evening,"Bharath")


