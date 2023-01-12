class Unit():
    def __init__(self , name, hp):
        self.name = name 
        self.hp == 100
    
    def heal(self):
       if self.mp > 0:
        self.hp += 5
        self.mp -= 2
        if self.hp < 100:
                self.hp = 100

    def attackFire(self , target ):
        target.hp -= 10


Unit = Unit("Petya")
print(Unit.hp, Unit.mp)
Unit.hp -= 20
print(Unit.hp, Unit.mp)
Unit.heal()
print(Unit.hp, Unit.mp)



