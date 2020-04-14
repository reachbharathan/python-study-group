def square_number_as_list(numList):
    result_list = []
    for num in numList:
        result_list.append((num * num)+1)
    return result_list

def square_number_as_generators(num_list):
    for num in num_list:
      yield((num * num)+1)

num_list = [1, 2, 3, 4, 5]
list_temp = square_number_as_list(num_list)
yeild_temp = square_number_as_generators(num_list)

# print(square_number_using_list(num_list))
print(list_temp)
print(yeild_temp)
print(next(yeild_temp))
print(next(yeild_temp))































# def square_number_using_yeild(numList):
#     for num in numList:
#         yield(num * num)


# square_number_using_list_com = [(x * x) for x in num_list]
# square_number_list = [(x * x) for x in num_list]
# square_number_generators = [(x * x) for x in num_list]

# print(square_number_using_list_com)
