class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main

class WokerTests(TestCase):
    def test_if_worker_initialized_correctly(self):
        worker = Worker("Test", 200, 20)
        self.assertEqual("Test", worker.name)
        self.assertEqual(200, worker.salary)
        self.assertEqual(20, worker.energy)
        self.assertEqual(0, worker.money)

    def test_if_worker_energy_is_incremented(self):
        worker = Worker("Test", 200, 20)
        self.assertEqual(20, worker.energy)

        worker.rest()

        self.assertEqual(21, worker.energy)

    def test_if_work_with_negative_energy_raises(self):
        worker = Worker("Test", 200, -1)


        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_work_with_zero_energy_raises(self):
        worker = Worker("Test", 200, 0)


        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_for_money_increment_after_work(self):
        worker = Worker("Test", 200, 20)

        self.assertEqual(0, worker.money)

        worker.work()

        self.assertEqual(200, worker.money)

    def test_if_energy_decreased_after_work(self):
        worker = Worker("Test", 200, 20)

        self.assertEqual(20, worker.energy)

        worker.work()

        self.assertEqual(19, worker.energy)

    def test_for_proper_get_info_return(self):
        worker = Worker("Test", 200, 20)

        self.assertEqual('Test has saved 0 money.', worker.get_info())
        worker.work()
        self.assertEqual('Test has saved 200 money.', worker.get_info())

if __name__ == "__main__":
    main()