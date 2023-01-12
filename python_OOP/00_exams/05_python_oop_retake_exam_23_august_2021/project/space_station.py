from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUTS = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }
    successful_missions = 0
    not_successful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type not in self.ASTRONAUTS:
            raise Exception("Astronaut type is not valid!")

        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            return f"{astronaut.name} is already added."

        astronaut = self.ASTRONAUTS[astronaut_type](name)
        self.astronaut_repository.add(astronaut)

        return f"Successfully added {astronaut_type}: {astronaut.name}."

    def add_planet(self, name, items):
        planet = self.planet_repository.find_by_name(name)

        if planet:
            return f"{name} is already added."

        planet = Planet(name)
        planet_items = items.split(", ")
        planet.items = planet_items
        self.planet_repository.planets.append(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.oxygen += 10

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        top_five_astronauts = sorted(
            [a for a in self.astronaut_repository.astronauts if a.oxygen > 30],
            key= lambda x: -x.oxygen
        )[:5]

        if not top_five_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_on_mission = 0

        for astronaut in top_five_astronauts:
            astronauts_on_mission +=1
            while astronaut.oxygen > 0:
                if not planet.items:
                    self.successful_missions += 1
                    return f"Planet: {planet_name} was explored. {astronauts_on_mission} astronauts participated in collecting items."

                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

        self.not_successful_missions += 1
        return "Mission is not completed."

    def report(self):
        output = [
            f"{self.successful_missions} successful missions!",
            f"{self.not_successful_missions} missions were not completed!",
            "Astronauts' info:"
        ]

        output.extend([repr(x) for x in self.astronaut_repository.astronauts])

        return '\n'.join(output)

