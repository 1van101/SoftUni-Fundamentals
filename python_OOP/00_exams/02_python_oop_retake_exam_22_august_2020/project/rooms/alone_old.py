from project.rooms.room import Room


class AloneOld(Room):

    def __init__(self, family_name, pension):
        super().__init__(family_name, pension, 1)
        self.room_cost = 10

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. " \
               f"Budget: {self.budget:.2f}$, " \
               f"Expenses: {self.expenses - self.room_cost:.2f}$\n" \
               f"--- Appliances monthly cost: {self.expenses - self.room_cost:.2f}$"
