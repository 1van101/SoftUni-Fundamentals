from unittest import TestCase, main
from list_structure import IntegerList

class IntegerListTests(TestCase):
    def test_constructor_with_incorrect_data(self):
        lst = IntegerList(0.5, "tests")
        self.assertEqual([], lst._IntegerList__data)

    def test_constructor_with_correct_data(self):
        lst = IntegerList(1, 2, "tests")
        self.assertEqual([1, 2], lst._IntegerList__data)

    def test_add_method_with_correct_data(self):
        lst = IntegerList(1, 2)
        result = lst.add(3)

        self.assertEqual([1, 2, 3], result)

        new_result = lst.add(4)

        self.assertEqual([1, 2, 3, 4], new_result)

    def test_add_method_with_float_raises(self):
        lst = IntegerList(1, 2)

        with self.assertRaises(ValueError) as ex:
            lst.add(3.5)
        self.assertEqual("Element is not Integer", str(ex.exception))


    def test_add_method_with_string_raises(self):
        lst = IntegerList(1, 2)

        with self.assertRaises(ValueError) as ex:
            lst.add("3")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_method_with_valid_index(self):
        lst = IntegerList(1, 2)
        result = lst.remove_index(0)

        self.assertEqual(1, result)
        self.assertEqual([2], lst._IntegerList__data)

    def test_remove_method_with_invalid_index_raises(self):
        lst = IntegerList(1, 2)

        with self.assertRaises(IndexError) as ex:
            lst.remove_index(2)

            self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_get_returns_correct_element(self):
        lst = IntegerList(1, 2)

        result = lst.get(0)

        self.assertEqual(1, result)

    def test_get_method_with_invalid_index_raises(self):
        lst = IntegerList(1, 2)

        with self.assertRaises(IndexError) as ex:

            lst.get(2)
            self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_insert_element(self):
        lst = IntegerList(1, 2)

        lst.insert(0, 0)

        self.assertEqual([0, 1, 2], lst._IntegerList__data)

    def test_insert_if_invalid_index_raises(self):
        lst = IntegerList(1, 2)

        with self.assertRaises(IndexError) as ex:
            lst.insert(2, 5)

            self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_if_invalid_element_raises(self):
        lst = IntegerList(1, 2)

        with self.assertRaises(ValueError) as ex:
            lst.insert(0, "5")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_if_get_biggest(self):
        lst = IntegerList(1, 2)

        result = lst.get_biggest()

        self.assertEqual(2, result)

    def test_if_get_index(self):
        lst = IntegerList(1, 2)

        result = lst.get_index(2)

        self.assertEqual(1, result)

if __name__ == "__main__":
    main()