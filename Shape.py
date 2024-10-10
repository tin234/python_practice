import math


# Базовый класс"
class Shape:

    
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter
    
    def get_area(self):
        return self.area
    
    def get_perimeter(self):
        return self.perimeter

# Класс "Круг"
class Circle(Shape):
    
    
    def __init__(self, radius):
        self.radius = radius
        
        """Площадь круга =  pi * r^2"""
        area = math.pi * self.radius ** 2
        
        """Длина(периметр) окружности = 2 * π * r"""
        perimeter = 2 * math.pi * self.radius

        super().__init__(area, perimeter)

# Класс "Квадрат"
class Square(Shape):

    
    def __init__(self, side_length):
        self.side_length = side_length
        
        """Площадь квадрата = a^2"""
        area = self.side_length ** 2
        
        """Периметр квадрата = 4 * a"""
        perimeter = 4 * self.side_length 

        super().__init__(area, perimeter)
        
# Класс "Прямоугольник"
class Rectangle(Shape):
    
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

        """Площадь прямоугольника = w * h"""
        area = self.width * self.height

        """Периметр прямоугольника =  2 * (w + h)"""
        perimeter = 2 * (self.width + self.height)

        super().__init__(area, perimeter)



print(f"Площадь круга: {Circle(5).get_area()}")           
print(f"Периметр круга: {Circle(5).get_perimeter()}")

print(f"Площадь квадрата: {Square(2).get_area()}")        
print(f"Периметр квадрата: {Square(2).get_perimeter()}")  

print(f"Площадь прямоугольника: {Rectangle(2, 4).get_area()}")        
print(f"Периметр прямоугольника: {Rectangle(2, 4).get_perimeter()}")
