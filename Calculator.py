class Calculator:
    
    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return a - b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @classmethod
    def divide(cls, a, b):
        if b == 0:
            return "Деление на ноль невозможно"
        return a / b

print("Сложение: 2 + 3 =", Calculator.add(2, 3))
print("Вычитание: 7 - 2 =", Calculator.subtract(7, 2))
print("Умножение: 4 * 5 =", Calculator.multiply(4, 5))
print("Деление: 10 / 2 =", Calculator.divide(10, 0))
print("Деление: 10 / 2 =", Calculator.divide(10, 2))
