lambda arguments: expression
# need to mention the arguments
# and the expression alone

def cube(y): # y is an argument
    return y*y*y; # has a return type of number

def add(a,b): # has two aruguments
    return a+b; # has a return type string or number

print(cube(5))
print(add("3","5"))

# tempList = [1,2,3,4,5];

# tempArry = [] # [1, 4, 9, 16, 25]

# def sqare(i):
#   return i*i;

# for j in tempList:
#   tempArry.append(sqare(j))

# print("tempArry")
# print(tempArry)



def cube(y): # regular function
    return y * y * y


def add(a,b):  # has two aruguments
    return a + b

def complex_addition(a,b):
    temp_a = a * 100
    temp_b = b * 100
    temp_a = temp_a + 3
    temp_b = temp_b + 3
    return temp_a + temp_b;

add = lambda a,b: a+b
cube = lambda x: x*x*x # lambda function
print("lambda function");
# print(cube(3));
# print(add(3,5));
print(complex_addition(3, 5))




# g = lambda x: x*x*x
# print(g(7))
