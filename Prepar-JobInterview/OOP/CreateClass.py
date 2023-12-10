name = "Haisbullah Aman"
age = '23'

class myName:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printMyName(self):
        print(f"my name is {self.name} and I'm {self.age} years old")
p1 = myName("Ali", 32)

print(p1.name)
print(p1.age)

p1.printMyName()

# __init__()