from Calculator_with_mixins import Calculator

class ConstantCalculator(Calculator):
    def add(self, a, b):
        return 1

    def subtract(self, a, b):
        return 2

    def multiply(self, a, b):
        return 3

    def divide(self, a, b):
        if b == 0:
            return "Деление на ноль невозможно"
        return 4
    

const_calc = ConstantCalculator()
print(const_calc.calculate(10, 5, '+'))  
print(const_calc.calculate(10, 5, '-'))  
print(const_calc.calculate(10, 5, '*'))
print(const_calc.calculate(10, 5, '/'))
print(const_calc.calculate(10, 0, '/'))
print(const_calc.calculate(10, 0, '%'))