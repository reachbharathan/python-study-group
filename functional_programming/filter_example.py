numArray = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

# def filter_Odd(numArray):
#     odd_list = [];
#     for i in numArray:
#         if i%2 != 0:
#             odd_list.append(i)
#     return odd_list

# print(filter_Odd(numArray))


# def isOdd(i):
#     if i%2 == 0:
#         return True


# temp = filter(isOdd, numArray)  # 5, 7, 97, 54, 62, 77, 23, 73, 61]
temp = filter(lambda i: i%2!=0, numArray)  # 5, 7, 97, 54, 62, 77, 23, 73, 61]
print(list(temp))













# print(list(filter(lambda x: (x%2 != 0) , numArray)))