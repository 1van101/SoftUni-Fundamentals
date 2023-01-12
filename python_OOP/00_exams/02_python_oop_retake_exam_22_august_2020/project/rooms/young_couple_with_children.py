from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.children = [*children]
        self.calculate_expenses(self.appliances, self.children)

    def __repr__(self):
        children_expenses = sum([x.cost * 30 for x in self.children])
        output = f"{self.family_name} with {self.members_count} members. " \
               f"Budget: {self.budget:.2f}$, " \
               f"Expenses: {self.expenses - self.room_cost:.2f}$\n"

        for i, child in enumerate(self.children, 1):
            output += f"--- Child {i} monthly cost: {child.cost * 30:.2f}$" + "\n"

        output += f"--- Appliances monthly cost: {self.expenses - self.room_cost - children_expenses:.2f}$"

        return output


