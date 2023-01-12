from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    fish_types = ["FreshwaterFish", "SaltwaterFish"]

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        return sum(x.comfort for x in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        if type(fish).__name__ in self.fish_types:
            self.fish.append(fish)
            return f"Successfully added {type(fish).__name__} to {self.__name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        output = [f'{self.name}:']
        output.append("Fish: none" if not self.fish else f"Fish: {' '.join(x.name for x in self.fish)}")
        output.append(f'Decorations: {len(self.decorations)}')
        output.append(f"Comfort: {self.calculate_comfort()}")

        return '\n'.join(output)
