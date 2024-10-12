class AddMixin:
    def add(self, a, b):
        return a + b


class SubtractMixin:
    def subtract(self, a, b):
        return a - b


class MultiplyMixin:
    def multiply(self, a, b):
        return a * b
    

class DivideMixin:
    def divide(self, a, b):
        if b == 0:
            return "Деление на ноль невозможно"
        return a / b


class Calculator(AddMixin, SubtractMixin, MultiplyMixin, DivideMixin):
    def calculate(self, a, b, operator):
        if operator == '+':
            return self.add(a, b)
        elif operator == '-':
            return self.subtract(a, b)
        elif operator == '*':
            return self.multiply(a, b)
        elif operator == '/':
            return self.divide(a, b)
        else:
            return "Неизвестное действие"

calc = Calculator()
print(calc.calculate(10, 5, '+'))  
print(calc.calculate(10, 5, '-'))  
print(calc.calculate(10, 5, '*'))
print(calc.calculate(10, 5, '/'))
print(calc.calculate(10, 0, '/'))
print(calc.calculate(10, 0, '%'))
