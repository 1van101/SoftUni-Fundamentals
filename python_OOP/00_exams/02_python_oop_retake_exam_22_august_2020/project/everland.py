class Everland:
    def __init__(self):
        self.rooms = []

    def total_population(self):
        return sum(x.members_count for x in self.rooms)

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        expenses = sum(room.expenses for room in self.rooms)

        return f"Monthly consumptions: {expenses:.2f}$."

    def pay(self):
        output = []
        rooms_to_be_removed = []

        for room in self.rooms:
            if room.budget >= room.expenses - room.room_cost:
                room.budget -= room.expenses
                output.append(
                    f"{room.family_name} paid {room.expenses:.2f}$ and have {room.budget:.2f}$ left.")

            else:
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_to_be_removed.append(room)

        self.rooms = [x for x in self.rooms if x not in rooms_to_be_removed]
        return '\n'.join(output)

    def status(self):
        output = [f"Total population: {self.total_population()}"]
        output.extend([repr(x) for x in self.rooms])
        return "\n".join(output)
