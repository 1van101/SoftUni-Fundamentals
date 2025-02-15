from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.__radius = r

    def calculate_area(self):
        return pi * self.__radius ** 2

    def calculate_perimeter(self):
        return pi * 2 * self.__radius


class Rectangle(Shape):
    def __init__(self, h, w):
        self.__height = h
        self.__width = w

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * self.__width + 2 * self.__height


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
