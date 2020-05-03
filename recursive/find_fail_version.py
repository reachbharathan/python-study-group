# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

#* create a function whcih a argument
# verify

def isFailure(x):
  if(x>=4):
    return False

case 1: 1,2,3,4,5  here starting from 4 the code is failure
4
isFailure(5) -> True
isFailure(4) -> True
isFailure(3) -> False

case 2: 1,2,3,4,5,...,100 here starting from 4 the code is failure
87
isFailure(88) -> True
isFailure(87) -> True

# O(1)
def mutliply (100):
  return 100*100

# O(2)
def complex_Multiply(n):
  if ( n<10):
      n= n*n
      return n*n # complexity 2
  else:
      return n*n # complexity 1

# o(n)
def create_arry(n):
  array= []
  for i in range(n):
    array.append(i)
  return array

# O(n^2)
def create_arry(n):
  array= []
  for i in range(n):
    for j in range(n):
      array.append(i+j) 
  return array
