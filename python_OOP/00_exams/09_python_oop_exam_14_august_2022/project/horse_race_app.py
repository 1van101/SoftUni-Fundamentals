from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSES_TYPES = ["Appaloosa", "Thoroughbred"]

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __check_if_horse_is_added(self, horse_name):
        try:
            searched_horse = [x for x in self.horses if x.name == horse_name][0]
            return searched_horse
        except IndexError:
            return False

    def __check_if_jockey_is_added(self, jockey_name):
        try:
            searched_jockey = [x for x in self.jockeys if x.name == jockey_name][0]
            return searched_jockey
        except IndexError:
            return False

    def __check_if_race_is_added(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return False

    def add_horse(self, horse_type, horse_name, horse_speed):
        if horse_type in HorseRaceApp.HORSES_TYPES:

            if self.__check_if_horse_is_added(horse_name):
                raise Exception(f"Horse {horse_name} has been already added!")

            horse_to_add = None
            if horse_type == "Appaloosa":
                horse_to_add = Appaloosa(horse_name, horse_speed)
            if horse_type == "Thoroughbred":
                horse_to_add = Thoroughbred(horse_name, horse_speed)

            self.horses.append(horse_to_add)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        if self.__check_if_jockey_is_added(jockey_name):
            raise ValueError(f"Jockey {jockey_name} has been already added!")

        jockey_to_add = Jockey(jockey_name, age)
        self.jockeys.append(jockey_to_add)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        if race_type in HorseRace.races_created:
            raise Exception(f"Race {race_type} has been already created!")

        new_horse_race = HorseRace(race_type)
        self.horse_races.append(new_horse_race)
        HorseRace.races_created.append(race_type)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        if not self.__check_if_jockey_is_added(jockey_name):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        current_type_horses = [x for x in self.horses if type(x).__name__ == horse_type]

        if not current_type_horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        searched_jockey = self.__check_if_jockey_is_added(jockey_name)

        if searched_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."


        searched_horse = [x for x in current_type_horses[::-1] if not x.is_taken]
        if searched_horse:

            searched_jockey.horse = searched_horse[0]
            searched_horse[0].is_taken = True
            return f"Jockey {jockey_name} will ride the horse {searched_horse[0].name}."
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        if not self.__check_if_race_is_added(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        if not self.__check_if_jockey_is_added(jockey_name):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = self.__check_if_jockey_is_added(jockey_name)
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        race = [x for x in self.horse_races if x.race_type == race_type][0]
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        if not self.__check_if_race_is_added(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        searched_race = self.__check_if_race_is_added(race_type)

        if len(searched_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        jockey_name, horse_speed, horse_name = ["", 0, ""]
        for jockey in searched_race.jockeys:
            if jockey.horse.speed > horse_speed:
                jockey_name = jockey.name
                horse_speed = jockey.horse.speed
                horse_name = jockey.horse.name

        return f"The winner of the {race_type} race, with a speed of {horse_speed}km/h is {jockey_name}! Winner's horse: {horse_name}."
