# myList = [2, 3, 7, 5, 6]
# print(len(myList))

# Method,Function, Operator  ---> we can use in different form


# Polymorphism mean that we use some method for different class

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Drive!")
#
# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Sail!")
#
# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Fly!")
#
# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class
#
# for x in (car1, boat1, plane1):
#   x.move()


class Vechile:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vechile):
    def move(self):
        print("move on street!")

class Boat(Vechile):
    def move(self):
        print("move on sea!")

class Plane(Vechile):
    def move(self):
        print("Fly!")



car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
    print(x.model)
    print(x.brand)
    # print(x)
    x.move()