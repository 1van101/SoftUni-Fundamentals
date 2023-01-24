from unittest import TestCase, main

from vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(80, 200)

    def test_init(self):
        vehicle = Vehicle(80, 200)

        self.assertEqual(80, vehicle.fuel)
        self.assertEqual(80, vehicle.capacity)
        self.assertEqual(200, vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_insufficient_fuel_raises(self):
        # self.assertEqual(80, self.vehicle.fuel)

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(self.vehicle.fuel)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        # distance = 50
        burned_fuel = 50 * self.vehicle.fuel_consumption
        fuel_expected = self.vehicle.fuel - burned_fuel

        self.assertEqual(80, self.vehicle.fuel)
        self.vehicle.drive(50)

        self.assertEqual(fuel_expected, self.vehicle.fuel)

    def test_if_refuel_with_more_of_the_capacity_raises(self):
        self.assertEqual(80, self.vehicle.fuel)

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_if_refuel_with_valid_quantity(self):
        self.assertEqual(80, self.vehicle.fuel)

        self.vehicle.fuel = 60

        self.assertEqual(60, self.vehicle.fuel)

        self.vehicle.refuel(20)

        self.assertEqual(80, self.vehicle.fuel)

    # def test_refueling_after_driving(self):
    #     self.vehicle.drive(10)
    #
    #     fuel_left = self.vehicle.fuel
    #
    #     self.vehicle.refuel(1)
    #
    #     self.assertEqual(fuel_left + 1, self.vehicle.fuel)

    def test_string_method(self):
        # expected = f"The vehicle has {self.vehicle.horse_power} horse power" \
        #            f" with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        expected = "The vehicle has 200 horse power with 80 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, str(self.vehicle))


if __name__ == "__main__":
    main()
