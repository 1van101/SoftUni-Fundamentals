class Circle:
    __pi = 3.14

    def __init__(self, d):
        self.d = d


    def calculate_circumference(self):
        return self.__pi * self.d


    def calculate_area(self):
        return self.__pi * (self.d / 2) ** 2


    def calculate_area_of_sector(self, angle):
        return (self.d / 2) ** 2 * self.__pi * (angle / 360)


angle = int(input())

circle = Circle(10)
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
