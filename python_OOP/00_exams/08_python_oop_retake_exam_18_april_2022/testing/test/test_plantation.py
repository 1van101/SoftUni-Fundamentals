from unittest import TestCase
from project.plantation import Plantation

class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(100)

    def test_size_setter_with_valid_data(self):
        self.assertEqual(100, self.plantation._Plantation__size)

    def test_size_setter_with_negative_data_raises(self):
        with self.assertRaises(ValueError) as ve:
            plantation = Plantation(-1)

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_when_worker_not_already_added(self):
        actual_result = self.plantation.hire_worker("worker1")

        self.assertEqual(["worker1"], self.plantation.workers)
        self.assertEqual("worker1 successfully hired.", actual_result)

    def test_hire_worker_when_worker_already_added_raises(self):
        self.plantation.hire_worker("worker1")
        self.plantation.hire_worker("worker2")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("worker1")

        self.assertEqual("Worker already hired!", str(ve.exception))
        self.assertEqual(["worker1", "worker2"], self.plantation.workers)

    def test_planting_if_worker_not_in_plants(self):
        self.plantation.hire_worker("worker1")
        self.plantation.hire_worker("worker2")

        actual_result = self.plantation.planting("worker1", "plant1")

        self.assertEqual({"worker1": ["plant1"]}, self.plantation.plants)
        self.assertEqual("worker1 planted it's first plant1.", actual_result)
        self.assertEqual("worker2 planted it's first plant2.", self.plantation.planting("worker2", "plant2"))
        self.assertEqual({"worker1": ["plant1"], "worker2": ["plant2"]}, self.plantation.plants)

    def test_planting_if_worker_in_plants(self):
        self.plantation.hire_worker("worker1")
        self.plantation.planting("worker1", "plant1")

        actual_result = self.plantation.planting("worker1", "plant2")

        self.assertEqual({"worker1": ["plant1", "plant2"]}, self.plantation.plants)
        self.assertEqual("worker1 planted plant2.", actual_result)

    def test_planting_if_worker_still_not_hired_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("worker1", "plant1")

        self.assertEqual("Worker with name worker1 is not hired!", str(ve.exception))

    def test_if_plant_is_full_raises(self):
        plantation = Plantation(1)

        plantation.hire_worker("worker1")
        plantation.planting("worker1", "plant1")

        with self.assertRaises(ValueError) as ve:
            plantation.planting("worker1", "plant2")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_len_method(self):
        self.plantation.hire_worker("worker1")
        self.plantation.hire_worker("worker2")
        self.plantation.planting("worker1", "plant1")
        self.plantation.planting("worker1", "plant2")
        self.plantation.planting("worker2", "plant3")

        self.assertEqual(3, len(self.plantation))

    def test_string_method(self):
        self.plantation.hire_worker("worker1")
        self.plantation.hire_worker("worker2")
        self.plantation.planting("worker1", "plant1")
        self.plantation.planting("worker2", "plant3")
        self.plantation.planting("worker1", "plant2")
        self.plantation.planting("worker2", "plant4")

        expected_result = "Plantation size: 100\nworker1, worker2\nworker1 planted: plant1, plant2\nworker2 planted: plant3, plant4"

        self.assertEqual(expected_result, str(self.plantation))

    def test_repr_method(self):
        self.plantation.hire_worker("worker1")
        self.plantation.hire_worker("worker2")

        expected_result = "Size: 100\nWorkers: worker1, worker2"

        self.assertEqual(expected_result, repr(self.plantation))