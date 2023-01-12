from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train("Train", 3)

    def test_init(self):
        self.assertEqual("Train", self.train.name)
        self.assertEqual(3, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_not_existing_passenger(self):
        actual_result = self.train.add("passenger1")

        self.assertEqual("Added passenger passenger1", actual_result)
        self.assertEqual("Added passenger passenger2", self.train.add("passenger2"))
        self.assertEqual(["passenger1", "passenger2"], self.train.passengers)

    def test_add_existing_passenger_raises(self):
        self.train.add("passenger1")

        with self.assertRaises(ValueError) as ve:
            self.train.add("passenger1")

        self.assertEqual("Passenger passenger1 Exists", str(ve.exception))
        self.assertEqual(["passenger1"], self.train.passengers)

    def test_add_passenger_no_capacity_raises(self):
        self.train.add("passenger1")
        self.train.add("passenger2")
        self.train.add("passenger3")

        with self.assertRaises(ValueError) as ve:
            self.train.add("passenger4")

        self.assertEqual("Train is full", str(ve.exception))
        self.assertEqual(["passenger1", "passenger2", "passenger3"], self.train.passengers)

    def test_remove_passenger(self):
        self.train.add("passenger1")
        self.train.add("passenger2")

        self.assertEqual(["passenger1", "passenger2"], self.train.passengers)

        actual_result = self.train.remove("passenger1")

        self.assertEqual("Removed passenger1", actual_result)
        self.assertEqual(["passenger2"], self.train.passengers)

    def test_remove_not_existing_passenger_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove("passenger1")

        self.assertEqual("Passenger Not Found", str(ve.exception))
        self.assertEqual([], self.train.passengers)


if __name__ == "__main__":
    main()
