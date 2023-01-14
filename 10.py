class Human():
    def __init__(self, name: str):
        self.name = name
        self.car: Car = None

    def buy_car(self, car):
        if isinstance(car, Car):
            self.car = car
        else:
            raise ValueError

    def drive(self):
        if self.car:
            self.car.drive()
        else:
            print(f"{self.name} is having no car")


class Car():
    def __init__(self, brand: str):
        self.brand = brand
        self.owner: Human = None

    def sell(self, human: Human):
        if isinstance(human, Human):
            self.owner = human
            self.owner.buy_car(self)
        else:
            raise ValueError
    
    def drive(self):
        if self.owner:
            print("Edy-Edyyyy!")
        else:
            print("Not owner protecta")


petya = Human("Petya")
BMW = Car("BMW")
BMW.sell(petya)

petya.drive()