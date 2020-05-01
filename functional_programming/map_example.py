numArray = [1, 2, 3, 4, 5]


# def squar_list(numArray):
#     squared = []
#     for i in numArray:
#         squared.append(i**2)
#     return squared

# def square(i):
#     return i*i;

# print(squar_list(numArray))

temp = map(lambda i: i * i, numArray)
print(list(temp))














# print(list(map(lambda x: x**2, numArray)))