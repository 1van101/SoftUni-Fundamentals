class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []


    def add_animal(self, species, animal_name):
        self.__animals += 1
        if species == "mammal":
            self.mammals.append(animal_name)
        elif species == "fish":
            self.fishes.append(animal_name)
        elif species == "bird":
            self.birds.append(animal_name)


    def get_info(self, species):
        animals_names = None
        species_type = ""
        if species == "mammal":
            species_type = "Mammals"
            animals_names = ", ".join(self.mammals)
        elif species == "fish":
            species_type = "Fishes"
            animals_names = ", ".join(self.fishes)
        elif species == "bird":
            species_type = "Bird"
            animals_names = ", ".join(self.birds)

        return f"""{species_type} in {self.name}: {animals_names}
Total animals: {self.__animals}"""


zoo_name = input()
n = int(input())
zoo = Zoo(zoo_name)

for x in range(n):
    current_animal = input().split()
    species = current_animal[0]
    animal_name = current_animal[1]
    zoo.add_animal(species, animal_name)

info = input()
print(zoo.get_info(info))