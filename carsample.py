class car:
    def __init__(self, name, model):
        self.name = name
        self.model = model


car1 = car("BMW", "X5")
car2 = car("Audi", "Q7")

for key , value in car1.__dict__.items():
    print(f"{key}: {value}")