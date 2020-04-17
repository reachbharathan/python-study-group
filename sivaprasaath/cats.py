class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
c1 = Cat("siva", 19)
c2 = Cat("ragul", 20)
c3 = Cat("bharath", 20)
def get_oldest_cat(*args):
    return max(args)
print(f"The oldest cat is {get_oldest_cat(c1.age, c2.age, c3.age)} years old.")
