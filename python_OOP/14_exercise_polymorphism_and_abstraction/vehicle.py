from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    def count_consumed_fuel(self, dist, AIR_CONDITIONER_ON):
        fuel_cons = dist * (self.fuel_consumption + AIR_CONDITIONER_ON)
        if self.fuel_quantity >= fuel_cons:
            self.fuel_quantity -= fuel_cons


class Car(Vehicle):
    def drive(self, distance):
        self.count_consumed_fuel(distance, 0.9)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def drive(self, distance):
        self.count_consumed_fuel(distance, 1.6)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
