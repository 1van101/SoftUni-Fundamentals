from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __check_for_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(f"Driver {driver_name} could not be found!")

    def __check_for_cars_by_type(self, car_type):
        cars = []
        for car in self.cars:
            if type(car).__name__ == car_type and not car.is_taken:
                cars.append(car)
        if cars:
            return cars

        raise Exception(f"Car {car_type} could not be found!")

    def __check_for_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

        raise Exception(f"Race {race_name} could not be found!")

    def create_car(self, car_type, model, speed_limit):
        if car_type not in Controller.VALID_CAR_TYPES:
            return

        if any([x.model == model for x in self.cars]):
            raise Exception(f"Car {model} is already created!")

        new_car = Controller.VALID_CAR_TYPES[car_type](model, speed_limit)
        self.cars.append(new_car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        if any([x.name == driver_name for x in self.drivers]):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        if any([x.name == race_name for x in self.races]):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver = self.__check_for_driver_by_name(driver_name)
        free_cars = self.__check_for_cars_by_type(car_type)

        new_driver_car = free_cars[-1]

        if driver.car:
            old_driver_car = driver.car
            old_driver_car.is_taken = False

            driver.car = new_driver_car
            new_driver_car.is_taken = True

            return f"Driver {driver.name} changed his car from {old_driver_car.model} to {new_driver_car.model}."
        else:
            driver.car = new_driver_car
            new_driver_car.is_taken = True

            return f"Driver {driver.name} chose the car {new_driver_car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race = self.__check_for_race_by_name(race_name)
        driver = self.__check_for_driver_by_name(driver_name)

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if any([x.name == driver_name for x in race.drivers]):
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self.__check_for_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        cars_in_race_sorted = sorted(race.drivers, key=lambda x: -x.car.speed_limit)

        output = ''

        for i in range(3):
            cars_in_race_sorted[i].number_of_wins += 1
            output += f"Driver {cars_in_race_sorted[i].name} wins the {race_name} race with a speed of {cars_in_race_sorted[i].car.speed_limit}." + "\n"

        return output.rstrip()
