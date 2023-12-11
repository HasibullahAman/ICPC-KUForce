class Vehicle:
    def __init__(self, name, model, color, passenger):
        self.name = name
        self.model = model
        self.color = color
        self.passenger = passenger

    def move(self):
        print(f'{self.name} moved')
