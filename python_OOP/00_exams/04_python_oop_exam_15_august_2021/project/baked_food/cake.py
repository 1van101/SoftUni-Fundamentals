from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    initial_size = 245

    def __init__(self, name, price):
        super().__init__(name, self.initial_size, price)