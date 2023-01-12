from unittest import TestCase, main

from project.bookstore import Bookstore


class BookstoreTests(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(100)

    def test_if_initializing_correct(self):
        self.assertEqual(100, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store._Bookstore__total_sold_books)

    def test_books_limit_setter_zero_limit_raises(self):

        with self.assertRaises(ValueError)as ve:
            Bookstore(0)

        expected_result = "Books limit of 0 is not valid"
        actual_result = str(ve.exception)
        self.assertEqual(expected_result, actual_result)

    def test_books_limit_setter_negative_limit_raises(self):

        with self.assertRaises(ValueError)as ve:
            Bookstore(-1)

        expected_result = "Books limit of -1 is not valid"
        actual_result = str(ve.exception)
        self.assertEqual(expected_result, actual_result)

    def test_len_method(self):
        self.store.availability_in_store_by_book_titles = {
            "Book1": 2,
            "Book2": 2,
            "Book3": 2
        }

        expected_result = sum(self.store.availability_in_store_by_book_titles.values())
        actual_result = len(self.store)
        self.assertEqual(expected_result, actual_result)

    def test_to_receive_book_if_there_is_enough_space(self):
        first_result = self.store.receive_book("Book1", 20)
        self.assertEqual({"Book1": 20}, self.store.availability_in_store_by_book_titles)
        self.assertEqual("20 copies of Book1 are available in the bookstore.", first_result)

        second_result = self.store.receive_book('Book1', 20)
        self.assertEqual({"Book1": 40}, self.store.availability_in_store_by_book_titles)
        self.assertEqual("40 copies of Book1 are available in the bookstore.", second_result)

        third_result = self.store.receive_book('Book2', 20)
        self.assertEqual({"Book1": 40, "Book2": 20}, self.store.availability_in_store_by_book_titles)
        self.assertEqual("20 copies of Book2 are available in the bookstore.", third_result)

    def test_to_receive_book_if_there_is_not_enough_space_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Book1", 101)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_to_sell_books_with_valid_data(self):
        self.store.receive_book("Book1", 50)

        first_actual_result = self.store.sell_book("Book1", 20)

        self.assertEqual({"Book1": 30}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(20, self.store._Bookstore__total_sold_books)
        self.assertEqual("Sold 20 copies of Book1", first_actual_result)

        second_actual_result = self.store.sell_book("Book1", 30)
        self.assertEqual({"Book1": 0}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(50, self.store._Bookstore__total_sold_books)
        self.assertEqual("Sold 30 copies of Book1", second_actual_result)

    def test_to_sell_books_with_not_existing_book_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Book1", 20)

        self.assertEqual("Book Book1 doesn't exist!", str(ex.exception))

    def test_to_sell_books_with_not_enough_copies_of_the_book_raises(self):
        self.store.receive_book("Book1", 10)

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Book1", 20)

        self.assertEqual("Book1 has not enough copies to sell. Left: 10", str(ex.exception))

    def test_string_method(self):
        self.store.receive_book("Book1", 10)
        self.store.receive_book("Book2", 10)
        self.store.receive_book("Book3", 10)
        self.store.sell_book("Book1", 10)

        expected_result = "Total sold books: 10\nCurrent availability: 20\n - Book1: 0 copies\n - Book2: 10 copies\n - Book3: 10 copies"
        actual_result = str(self.store)

        self.assertEqual(expected_result, actual_result)

if __name__ =="__main__":
    main()