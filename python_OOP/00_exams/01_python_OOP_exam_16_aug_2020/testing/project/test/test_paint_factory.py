from unittest import TestCase

from project_for_movies.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Name", 100)

    def test_if_initialising_correct(self):
        self.assertEqual("Name", self.paint_factory.name)
        self.assertEqual(100, self.paint_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_to_add_ingredient_with_valid_data(self):
        self.paint_factory.add_ingredient("white", 20)

        self.assertEqual({"white": 20}, self.paint_factory.ingredients)

        self.paint_factory.add_ingredient("white", 20)
        self.paint_factory.add_ingredient("yellow", 20)

        self.assertEqual({"white": 40, "yellow": 20}, self.paint_factory.ingredients)

    def test_to_add_ingredient_with_not_enough_space_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.paint_factory.add_ingredient("white", 200)

        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_to_add_ingredient_with_wrong_product_type_raises(self):
        with self.assertRaises(TypeError) as te:
            self.paint_factory.add_ingredient("orange", 20)

        self.assertEqual("Ingredient of type orange not allowed in PaintFactory", str(te.exception))

    def test_products_property(self):
        self.paint_factory.add_ingredient("white", 20)

        self.assertEqual({"white": 20}, self.paint_factory.products)

    def test_to_remove_ingredient_valid_data(self):
        self.paint_factory.add_ingredient("white", 20)
        self.paint_factory.add_ingredient("yellow", 20)

        self.assertEqual({"white": 20, "yellow": 20}, self.paint_factory.ingredients)

        self.paint_factory.remove_ingredient("yellow", 10)
        self.paint_factory.remove_ingredient("white", 20)

        self.assertEqual({"white": 0, "yellow": 10}, self.paint_factory.ingredients)

    def test_to_remove_ingredient_with_capacity_less_than_given_raises(self):
        self.paint_factory.add_ingredient("white", 20)

        with self.assertRaises(ValueError) as ve:
            self.paint_factory.remove_ingredient("white", 21)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_to_remove_ingredient_with_not_existing_ingredient_raises(self):
        with self.assertRaises(KeyError) as ke:
            self.paint_factory.remove_ingredient("white", 21)

        self.assertEqual("No such ingredient in the factory", str(ke.exception))

    def test_repr_method(self):
        self.paint_factory.add_ingredient("white", 20)
        self.paint_factory.add_ingredient("yellow", 20)
        expected_result = "Factory name: Name with capacity 100.\n" \
                          "white: 20\n" \
                          "yellow: 20\n"
        self.assertEqual(expected_result, repr(self.paint_factory))