class Human():
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.armor = 10
        self.points = 15
        self.mana = 10
        self.resources = 15

    def handKick(self, target):
        target.hp -= 10

class Warriors(Human):
    def __init__(self, name):
        super(name)
        self.hp = 120
        self.armor = 15
        self.points = 20
        self.points +=5
        self.resources = 15

    def StickAttack(self, target):
        target.hp -= 18

    def evasion(self):
        self.save_hp = 120

class Peasants(Human):
    def __init__(self, name):
        super(name)
        self.hp = 140
        self.armor = 20
        self.points = 35
        self.points +=15
        self.resources = 15

    def maceAttack(self, target):
        target.hp -= 30

    def evasion(self):
        self.save_hp = 140
    
    def bonus(self):
        self.mana += 15

class Spearman(Human):
    def __init__(self, name):
        super(name)
        self.hp = 145
        self.armor = 25
        self.points = 45
        self.points +=20
        self.resources = 15

    def spearAttack(self, target):
        target.hp -= 50

    def evasion(self):
        self.save_hp = 145
    
    def throw(self):
        self.throw -= 30

class Swordsman(Human):
    def __init__(self, name):
        super(name)
        self.hp = 160
        self.armor = 50
        self.points = 50
        self.points +=25
        self.resources = 15

    def swordAttack(self, target):

        target.hp -= 10

    def evasion(self):
        self.save_hp = 160
    
    def swipeAttack(self):
        self.swipeAttack -= 45
    
    def headAttack(self):
        self.headAttack -= 20
    
class Farmer(Human):
    def __init__(self, name):
        super(name)
        self.hp = 105
        self.armor = 12
        self.points = 25
        self.poits += 30
        self.resources = 15
        self.resources += 100

    def pitforckAttack(self, target):
        target.hp -= 25

    def protectionPitforck(self):
        self.save_hp = 105
    
    def headAttack(self):
        self.headAttack -= 10

    class Breeder(Human):
     def __init__(self, name):
        super(name)
        self.hp = 105
        self.armor = 12
        self.points = 25
        self.poits += 30
        self.resources = 15
        self.resources += 100

    def legsAttack(self):
        self.legsAttack -= 20

    def save_hp(self):
        self.save_hp = 105
    
    def headAttack(self):
        self.headAttack -= 10
    
    def heandAttack(self):
        self.heandAttack -= 15

    




















#! Human  - основной

#! Warriors - наследуется от человека

#! Peasants - наследуется от человека

#! Spearman - наследуется от воина

#! Swordsman - наследуется от воина

#! Farmer - наследуется от крестьянина

#! Breeder - наследуется от крестьянина



#! +2 Класса на выбор

#! Каждый класс имеет какое-то отличие от другого (Функция, аттрибут)






