from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        self.appliances = [TV()] * 1
        self.calculate_expenses(self.appliances)

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. " \
               f"Budget: {self.budget:.2f}$, " \
               f"Expenses: {self.expenses - self.room_cost:.2f}$\n" \
               f"--- Appliances monthly cost: {self.expenses - self.room_cost:.2f}$"

