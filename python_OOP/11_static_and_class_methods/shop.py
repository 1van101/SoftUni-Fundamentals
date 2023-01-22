class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, name):
        if sum(self.items.values()) == self.capacity:
            return "Not enough capacity in the shop"
        try:
            self.items[name] += 1
        except KeyError:
            self.items[name] = 1
        return f"{name} added to the shop"

    def remove_item(self, item_name, amount):
        try:
            if self.items[item_name] < amount:
                return f"Cannot remove {amount} {item_name}"
            if self.items[item_name] > amount:
                self.items[item_name] -= amount
            elif self.items[item_name] == amount:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the shop"
        except KeyError:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

import unittest

class ShopTests(unittest.TestCase):
    def setUp(self):
        self.fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)

    def test_add_item_success(self):
        result = self.fresh_shop.add_item("Bananas")
        self.assertEqual(self.fresh_shop.items["Bananas"], 1)
        self.assertEqual(result, "Bananas added to the shop")

    def test_remove_item_success(self):
        self.fresh_shop.add_item("Bananas")
        result = self.fresh_shop.remove_item("Bananas", 1)
        self.assertEqual(result, "1 Bananas removed from the shop")

    def test_remove_item_unsuccessful(self):
        self.fresh_shop.add_item("Bananas")
        result = self.fresh_shop.remove_item("Tomatoes", 2)
        self.assertEqual(result, "Cannot remove 2 Tomatoes")

    def test_repr(self):
        self.assertEqual(repr(self.fresh_shop), "Fresh Shop of type Fruit and Veg with capacity 50")


if __name__ == "__main__":
    unittest.main()