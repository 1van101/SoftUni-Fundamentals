from project.drink.drink import Drink


class Tea(Drink):
    costs = 2.50

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, self.costs, brand)
