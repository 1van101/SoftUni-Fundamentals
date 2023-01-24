from unittest import TestCase, main
from car_manager import Car


class CarTests(TestCase):
    def setUp(self) -> None:
        self.car = Car("BMW", "X6", 20, 80)

    def test_constructor(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("X6", self.car.model)
        self.assertEqual(20, self.car.fuel_consumption)
        self.assertEqual(80, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_with_empty_car_make_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    #
    def test_with_valid_car_make(self):
        car = Car("Audi", "X6", 20, 80)
        car.make = "BMW"
        self.assertEqual("BMW", car.make)

    def test_with_empty_car_model_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_with_zero_fuel_consumption_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_with_negative_fuel_consumption_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_with_negative_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_with_zero_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_with_negative_fuel_amount_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_with_valid_fuel_amount(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.car.fuel_amount = 10

        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_with_valid_quantity(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.car.refuel(20)

        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_with_negative_quantity_raises(self):
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-20)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_more_than_capacity(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.car.refuel(81)
        self.assertEqual(80, self.car.fuel_amount)

    def test_drive_with_enough_fuel(self):
        self.car.fuel_amount = 500

        self.car.drive(200)

        self.assertEqual(460, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(200)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
