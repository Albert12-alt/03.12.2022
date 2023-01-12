class Door():

    def __init__(self, size, Color, material, pattern, name):

        self.name = name
        self.size = size
        self.Color = Color
        self.material = material
        self.pattern = pattern

    def open(self):
        print(F"{self.name} открывается")

    def cloose(self):
        print(F"{self.name} закрывается")

class CompartmentDoor(Door):

    def __init__(self):

        pass

d = Door("size", "color", "material", "pattern", "name")
d.open()
d.cloose()