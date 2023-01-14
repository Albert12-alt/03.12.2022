import math




class Calculator:

    def summary(self, a, b) -> float:

        return float(a + b)



    def substraction(self, a, b) -> float:

        return float(a - b)



    def multiply(self, a, b) -> float:

        return float(a * b)



    def divide(self, a, b) -> float:

        return float(a / b)

    def Exponentiation(self, a, b , c , d) -> float:

        return float(a * b * c * d)
    
    def Root(self, a, b , c ) -> float:

        return float(a * b * c)

    def Module(self, a, b , c ) -> float:

        return float(a * b * c)

    def x(self, a, b , c ) -> float:

        return float(a * b * c)

class EngineeringCalculator(Calculator):

    def __init__(self):

        super()


    def Exponentiation(self, a, b , c , d) -> float:

        return float(a * b * c * d)
    
    def Root(self, a, b , c ) -> float:

        return float(a * b * c)

    def Module(self, a, b , c ) -> float:

        return float(a * b * c)

    def x(self, a, b , c ) -> float:

        return float(a * b * c)
    # Возведение в степень

    # Корень

    # Модуль

    # 10 * x

    # ...




calc = Calculator()

print(calc.summary(2, 2))

print(calc.substraction(2, 2))

print(calc.multiply(2, 2.0))

print(calc.divide(2, 2))

print(calc.summary((-2) * (-2) * (-2) * (-2)))

print(calc.summary(2 * 2 * 2))

print(calc.summary(3 * 1))

print(calc.summary(10 * 2))

ecalc = EngineeringCalculator()

