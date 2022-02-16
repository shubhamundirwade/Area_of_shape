#importing math for mathematical operation(pi)
import math

#Creating parent class
class Shape:

    def __init__(self, color='Red'):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

#creating child class for Rectangel by taking info from parent class
class Rectangle(Shape):

    def __init__(self, length, breadth):
        #with super() we call parent class  
        super().__init__()              
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_breadth(self):
        return self.__breadth

    def set_breadth(self, breadth):
        self.__breadth = breadth

    def get_area(self):
        return self.__length * self.__breadth

    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)


#creating child class for Circle by taking info from parent class
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


rectangle1 = Rectangle(15, 4)

print("Area of rectangle rectangle1: ", rectangle1.get_area())
print("Perimeter of rectangle rectangle1: ", rectangle1.get_perimeter())
print("Color of rectangle rectangle1: ", rectangle1.get_color())
rectangle1.set_color("Green")
print("Color of rectangle rectangle1: ", rectangle1.get_color())

circle1 = Circle(8)

print("\nArea of circle circle1: ", format(circle1.get_area(), "0.2f"))
print("Perimeter of circle circle1: ", format(circle1.get_perimeter(), "0.2f"))
print("Color of circle circle1: ", circle1.get_color())
circle1.set_color("Black")
print("Color of circle circle1: ", circle1.get_color())