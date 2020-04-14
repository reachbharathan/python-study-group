class Animal:
  name = "animal"
# a = 1
# x = [1,2,3]
# animalObj = Animal()
x = iter([1, 2, 3])

print(x)
# iterator pointer index -> 0
print(next(x)) # after this execution 
# iterator pointer index -> 1
print(next(x))
