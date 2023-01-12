from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * 2
        self.calculate_expenses(self.appliances)

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. " \
               f"Budget: {self.budget:.2f}$, " \
               f"Expenses: {self.expenses - self.room_cost:.2f}$\n" \
               f"--- Appliances monthly cost: {self.expenses - self.room_cost:.2f}$"

