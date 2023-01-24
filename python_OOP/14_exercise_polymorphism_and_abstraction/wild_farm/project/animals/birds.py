from animals import Bird
from food import Food


class Owl(Bird):
    allowed_foods = ['Meat']
    weight_coefficient = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    allowed_foods = [cls.__name__ for cls in Food.__subclasses__()]
    weight_coefficient = 0.35

    def make_sound(self):
        return "Cluck"
