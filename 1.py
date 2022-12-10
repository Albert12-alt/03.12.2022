class Monster():
    def __init__(self, name, hp, mp, offense, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.mp = mp
        self.offense = offense
        self.defense = defense

    def heal(self, value):
        #! Добавить к жизни значение
        #! Проверить, чтобы не было больше, чем в начале
        self.hp += value
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def getDamage(self, value):
        #! Если hp будет меньше или равно 0, то тогда пишем, что монстр погиб
        self.hp -= value
        if self.hp <= 0:
            print(f"{self.name} погиб")


m1 = Monster(name="Минотавр Легкий", hp=10, mp=10, offense=10, defense=10)
m2 = Monster("Минотавр Средний", 20, 20, 20, 20)

print(m2.hp)
m2.heal(value=10)
print(m2.hp)
m2.heal(value=10)
print(m2.hp)
m2.heal(value=10)
print(m2.hp)
m2.hp = 7
print(m2.hp)
m2.heal(value=10)
print(m2.hp)
m2.heal(value=10)
print(m2.hp)
m2.getDamage(value=5)
print(m2.hp)
m2.getDamage(value=5)
print(m2.hp)
m2.getDamage(value=5)
print(m2.hp)
m2.getDamage(value=5)
print(m2.hp)
