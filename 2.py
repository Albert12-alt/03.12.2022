class Frog():

    def init(self, name, age , size , Jumprange , color ):

        self.name = name

        self.age = age

        self.size = size

        self.Jumprange = Jumprange

        self.color = color

        print(f"Собаку зовут {self.name}")

    def sleep(self):
        print(f"{self.name} спит")

    def run(self):
        print(f"{self.name} бежит")
    
    def Jumprange(self):
        print(f"{self.name} прыгает")


    def greeting(self):
         print(f" лягушку зовут{self.name}. ей {self.age}")



#Frog1 = Frog(name="Карк", age="3" , size="15 сантиметров", Jumprange="10 сантиметров" , color="зеленый" )

#Frog1.greeting()

Frog1 = Frog
Frog1.name