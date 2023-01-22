from project import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, number, people):
        searched_room = [x for x in self.rooms if x.number == number][0]
        return searched_room.take_room(people)

    def free_room(self, number):
        searched_room = [x for x in self.rooms if x.number == number][0]
        return searched_room.free_room()

    def status(self):
        self.guests = sum([x.guests for x in self.rooms])
        free_rooms = []
        taken_rooms = []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(room.number)
            else:
                free_rooms.append(room.number)
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(x) for x in free_rooms)}\n" \
               f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}"


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
