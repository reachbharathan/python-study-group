import functools

numArray = [1,2,3,4,5]
# 1*2*3*4*5 = 120

def get_prodcut(numArray):
    x = 1
    for i in numArray:
        x = x*i
    return x

# print(get_prodcut(numArray))

def multiply(a,b):
    print("**********")
    print("a:",a)
    print("b:",b)
    print("**********")
    b= a*b
    return b  # 3 6
# [10,2,3,4,5]

# print(functools.reduce(multiply, numArray))


print(functools.reduce((lambda x,y: y*x), numArray,2))
