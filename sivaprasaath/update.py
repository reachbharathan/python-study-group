class human:
    def __init__(self):
        self.name="siva"
        self.age=19 

    def update(self):
        self.age=30

h1=human()
h2=human()
h2.name="ragul"
h2.update()
print(h1.name)
print(h2.name)
print(h1.age)
print(h2.age)