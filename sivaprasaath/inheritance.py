class User:
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self,name,power):
        self.name= name
        self.power= power

    def attack(self):
        print(f'attacking with the power of {self.power}')

class Archer(User):
    def __init__(self,name,num_arrows):
        self.name= name
        self.num_arrows= num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows lest-{self.num_arrows}')

Wizard1=Wizard('siva',50)
archer1=Archer('ragul',100)
Wizard1.attack()
archer1.attack()
print(isinstance(Wizard1,Wizard))


