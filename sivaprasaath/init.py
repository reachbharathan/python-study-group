class phone:
    def __init__(self,mp,ram):
        self.mp=mp
        self.ram=ram


    def config(self):
        print("config is",self.mp,self.ram)

phn1=phone(48,16)
phn2=phone(48,12)
phn1.config()
phn2.config()
print(type(phn1)) 