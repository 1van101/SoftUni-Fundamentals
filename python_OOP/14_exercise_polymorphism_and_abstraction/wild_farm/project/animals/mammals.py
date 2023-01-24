from project import Mammal


class Mouse(Mammal):
    allowed_foods = ['Vegetable', 'Fruit']
    weight_coefficient = 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    allowed_foods = ['Meat']
    weight_coefficient = 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    allowed_foods = ['Vegetable', 'Meat']
    weight_coefficient = 0.3

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    allowed_foods = ['Meat']
    weight_coefficient = 1

    def make_sound(self):
        return "ROAR!!!"
