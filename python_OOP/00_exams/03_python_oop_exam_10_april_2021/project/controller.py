from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    aquariums_types = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }
    decoration_types = {
        "Ornament": Ornament,
        "Plant": Plant
    }
    fish_types = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in self.aquariums_types:
            return "Invalid aquarium type."

        new_aquarium = self.aquariums_types[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in self.decoration_types:
            return "Invalid decoration type."

        new_decoration = self.decoration_types[decoration_type]()
        self.decorations_repository.decorations.append(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        # searched_decoration = [x for x in self.decorations_repository.decorations if
        #                        type(x).__name__ == decoration_type]
        searched_decoration = self.decorations_repository.find_by_type(decoration_type)
        searched_aquarium = [x for x in self.aquariums if x.name == aquarium_name]

        if searched_decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        if searched_aquarium:
            searched_aquarium[0].decorations.append(searched_decoration)
            self.decorations_repository.decorations.remove(searched_decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in self.fish_types:
            return f"There isn't a fish of type {fish_type}."

        new_fish = self.fish_types[fish_type](fish_name, fish_species, price)
        searched_aquarium = [x for x in self.aquariums if x.name == aquarium_name]

        if searched_aquarium:
            aquarium = searched_aquarium[0]

            if (fish_type == "FreshwaterFish" and type(aquarium).__name__ != "FreshwaterAquarium") or \
                    (fish_type == "SaltwaterFish" and type(aquarium).__name__ != "SaltwaterAquarium"):
                return "Water not suitable."

            return aquarium.add_fish(new_fish)
            # return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name):
        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        total_count_fish = 0

        for current_aquarium in self.aquariums:
            total_count_fish += len(current_aquarium.fish)

        aquarium.feed()
        return f"Fish fed: {total_count_fish}"

    def calculate_value(self, aquarium_name):
        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        total_value = 0
        for decoration in aquarium.decorations:
            total_value += decoration.price

        for fish in aquarium.fish:
            total_value += fish.price

        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        output = []
        for aquarium in self.aquariums:
            output.append(str(aquarium))

        return '\n'.join(output)

