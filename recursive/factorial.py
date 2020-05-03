import unittest
# factorial.py
# 5 -> 120
# 10 -> 3628800

# create function which accepts number
# make a if condition check number is 0 return 1
# esle n * fact(n-1)
# any function which call itself is called recuresive
# Condition for recuriive funciton
# it shoudl have a exit condition
# ensure the loop come to an end

def fact(n):
  if(n==1 or n==0):
    return 1
  else:
    return (n*fact(n-1))

assert (fact(5)==120)
assert (fact(0)==1)
assert (fact(1)==2)