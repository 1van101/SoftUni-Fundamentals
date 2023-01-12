from unittest import TestCase

from project.shopping_cart import ShoppingCart


class ShoppingCartTests(TestCase):
    def setUp(self) -> None:
        self.shop = ShoppingCart("Test", 100)

    def test_setter_for_name_invalid_data_raises(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("tes7", 100)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_invalid_data_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart("product1", 100)

        self.assertEqual("Product product1 cost too much!", str(ve.exception))

    def test_add_to_cart_valid_data(self):
        result = self.shop.add_to_cart("product1", 10)

        self.assertEqual({"product1": 10}, self.shop.products)
        self.assertEqual("product1 product was successfully added to the cart!", result)

        new_result = self.shop.add_to_cart("product2", 10)
        self.assertEqual({"product1": 10, "product2": 10}, self.shop.products)
        self.assertEqual("product2 product was successfully added to the cart!", new_result)

    def test_remove_invalid_product_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.remove_from_cart("product1")

        self.assertEqual("No product with name product1 in the cart!", str(ve.exception))

    def test_remove_valid_product(self):
        self.shop.add_to_cart("product1", 10)
        self.shop.add_to_cart("product2", 10)

        result = self.shop.remove_from_cart("product1")

        self.assertEqual({"product2": 10}, self.shop.products)
        self.assertEqual("Product product1 was successfully removed from the cart!", result)

    def test_add_method(self):
        self.shop.add_to_cart("product1", 20)
        other_shop = ShoppingCart("Othertest", 100)
        other_shop.add_to_cart("product1", 30)
        other_shop.add_to_cart("product2", 20)
        merged_shop = self.shop + other_shop

        self.assertEqual("TestOthertest", merged_shop.shop_name)
        self.assertEqual({"product1": 30, "product2": 20}, merged_shop.products)
        self.assertEqual(200, merged_shop.budget)

    def test_buy_with_invalid_data_raises(self):
        self.shop.products = {"product1": 300, "product2": 20}

        with self.assertRaises(ValueError) as ve:
            self.shop.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 220.00lv!", str(ve.exception))

    def test_buy_with_valid_data(self):
        self.shop.products = {"product1": 30, "product2": 20}

        result = self.shop.buy_products()

        self.assertEqual('Products were successfully bought! Total cost: 50.00lv.', result)
