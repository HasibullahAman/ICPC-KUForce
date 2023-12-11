class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def AsPerson(self):
        print(f"I am {self.name} and I'm {self.age} Year's old!")



class Student(person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.yearsGraduated = 2023
    def AsStudent(self):
        print(f"I am {self.name} and I'm {self.age} Year's old! and I graduated in {self.yearsGraduated}")


p1 = Student('Ali',23)
print(p1.AsStudent())
