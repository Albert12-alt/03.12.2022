class Class():

 def __init__(self, name):
    self.name = name
    self.points = 20
    self.hp = 100
def handKick(self):
    pass

class knight(Class):
       def __int__(self , name):
        super(name)
        self.hp = 150

       def  swordAttack(self):
        self.sword_attack = 20

       def  shieldAttack(self):
        self.shield_attack = 10

       def  evasion(self):
        self.save_hp = 140

class  Magus(Class):
       def __int__(self , name):
              super(name)
              self.points += 5
              self.hp = 200
       def  fireballAttack(self):
              self.fireball_attack = 40

       def  teleport(self):
              self.save_hp = 200

class  Archer(Class):
       def __int__(self , name):
              super(name)
              self.hp = 130

       def  ArcheryAttack(self):
              self.fireball_attack = 15

       def  unhide(self):
              self.name = self.bufer