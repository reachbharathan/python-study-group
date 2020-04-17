def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a , b):
   return a * b

def divide(a, b):
   return a / b, a % b, a // b
  
print("Available operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Please select a choice(1/2/3/4) from: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try:
    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))
        
    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
        print(num1 % num2)
        print(num1 // num2)

    else:
        print("Invalid input")

except ValueError:
    print("please check your input")
print("thank you")