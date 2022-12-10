import time

import random

if self.gladness < 100:
    self.gladness = 0 
else
    self.progress< 100:
self.progress = 0



class Student():

    def __init__(self, name):

        self.name = name

        self.gladness = 50  # %

        self.progress = 0  # %



    def study(self):
        random.randint(1,10)
        self.progress +=(random.randint(1,10))
        self.gladness -=(random.randint(1,10))
        # Повышается progress, но не может быть выше 100 (рандомно на 1-10)

        # Но понижается gladness, но не ниже 0 (рандомно на 1-10)

        print(

            f"{self.name} учится. Прогресс - {self.progress} | Счастье - {self.gladness}")



    def rest(self):
        self.gladness +=(random.randint(1,10))
        self.progress -=(random.randint(1,10))

        # Повышается gladness, но не может быть выше 100 (рандомно на 1-10)

        # Но понижается progress, но не ниже 0 (рандомно на 1-10)

        print(

            f"{self.name} отдыхает. Прогресс - {self.progress} | Счастье - {self.gladness}")




students = [

    Student("Антон"),

    Student("Артем"),

    Student("Олег"),

]



day = 1

while True:

    print(f"Day: {day}")

    for student in students:
        random.randint(print.rest, study)

        # Случайно студент или отдыхает или учится

        # student.rest()

        # student.study()

        pass

    day += 1

    time.sleep(0.1)