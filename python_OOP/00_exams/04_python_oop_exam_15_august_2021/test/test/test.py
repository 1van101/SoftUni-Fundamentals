from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("Test")

    def test_add_food_valid_data(self):
        actual_result = self.shop.add_food("food1", 10)

        self.assertEqual("Successfully added 10.00 grams of food1.", actual_result)
        self.assertEqual({"food1": 10}, self.shop.food)

        actual_second_result = self.shop.add_food("food1", 20)

        self.assertEqual("Successfully added 20.00 grams of food1.", actual_second_result)
        self.assertEqual({"food1": 30}, self.shop.food)

        self.assertEqual("Successfully added 50.00 grams of food2.", self.shop.add_food("food2", 50))
        self.assertEqual({"food1": 30, "food2": 50}, self.shop.food)

    def test_add_food_invalid_data_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("food1", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))
        self.assertEqual({}, self.shop.food)

    def test_add_pet_with_not_existing_pet(self):
        actual_result = self.shop.add_pet("pet1")

        self.assertEqual("Successfully added pet1.", actual_result)
        self.assertEqual(["pet1"], self.shop.pets)

    def test_add_pet_with_existing_pet_raises(self):
        self.shop.add_pet("pet1")
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("pet1")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_if_pet_and_food_exist(self):
        self.shop.add_pet("pet1")
        self.assertEqual(["pet1"], self.shop.pets)

        self.shop.add_food("food1", 100)
        self.assertEqual({"food1": 100}, self.shop.food)

        result = self.shop.feed_pet("food1", "pet1")

        self.assertEqual("pet1 was successfully fed", result)
        self.assertEqual({"food1": 0}, self.shop.food)

    def test_feed_pet_if_pet_exist_and_food_exist_but_not_enough_quantity(self):
        self.shop.add_pet("pet1")
        self.assertEqual(["pet1"], self.shop.pets)

        self.shop.add_food("food1", 10)
        self.assertEqual({"food1": 10}, self.shop.food)

        result = self.shop.feed_pet("food1", "pet1")

        self.assertEqual({"food1": 1010.0}, self.shop.food)
        self.assertEqual("Adding food...", result)

    def test_feed_pet_if_pet_doesnt_exist_raises(self):
        self.shop.add_food("food1", 200)
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("food1", "pet1")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_if_food_doesnt_exist_raises(self):
        self.shop.add_pet("pet1")

        result = self.shop.feed_pet("food1", "pet1")

        self.assertEqual('You do not have food1', result)

    def test_repr_method(self):
        self.shop.add_pet("pet1")
        self.shop.add_pet("pet2")

        expected_result = 'Shop Test:\n' \
                          'Pets: pet1, pet2'

        self.assertEqual(expected_result, repr(self.shop))


if __name__ == "__main__":
    main()
