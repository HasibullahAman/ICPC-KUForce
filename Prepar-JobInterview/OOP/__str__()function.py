class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'my name is {self.name} and Im {self.age} years old'
    def definationName(self):
        print(f"this Person {self.name} is so good person")
        print(f'she is {self.age} years old')


p2 = Person("Elhama", 22)

p3 = Person("Qasim",54)
p3.age = 45
p3.definationName()

# print(p2)
