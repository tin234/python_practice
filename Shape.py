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
    
    
    def get_area(self):
        return math.pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
    def __init__(self, radius):
        self.radius = radius
    

# Класс "Квадрат"
class Square(Shape):

    
    def __init__(self, side_length):
        self.side_length = side_length
        
    def get_area(self):
        return self.side_length ** 2
        
    def get_perimeter(self):
        return 4 * self.side_length 
    
        
# Класс "Прямоугольник"
class Rectangle(Shape):
    
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


print(f"Площадь круга: {Circle(5).get_area()}")           
print(f"Периметр круга: {Circle(5).get_perimeter()}")

print(f"Площадь квадрата: {Square(2).get_area()}")        
print(f"Периметр квадрата: {Square(2).get_perimeter()}")  

print(f"Площадь прямоугольника: {Rectangle(2, 4).get_area()}")        
print(f"Периметр прямоугольника: {Rectangle(2, 4).get_perimeter()}")
