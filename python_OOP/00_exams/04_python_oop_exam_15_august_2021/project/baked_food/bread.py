from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    initial_size = 200

    def __init__(self, name, price):
        super().__init__(name, self.initial_size, price)


