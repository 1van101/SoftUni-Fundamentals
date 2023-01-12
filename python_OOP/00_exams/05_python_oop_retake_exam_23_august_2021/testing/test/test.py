from unittest import TestCase

from project.library import Library


class LibraryTests(TestCase):
    def setUp(self) -> None:
        self.library = Library("Library")

    def test_setter_for_name_raises(self):
        with self.assertRaises(ValueError) as ve:
            Library("")

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_method(self):
        self.library.add_book("Author1", "Book1")

        self.assertEqual({"Author1": ["Book1"]}, self.library.books_by_authors)

        self.library.add_book("Author1", "Book2")

        self.assertEqual({"Author1": ["Book1", "Book2"]}, self.library.books_by_authors)

        self.library.add_book("Author1", "Book1")

        self.assertEqual({"Author1": ["Book1", "Book2"]}, self.library.books_by_authors)

    def test_add_reader_with_new_reader(self):
        self.library.add_reader("Reader1")

        self.assertEqual({"Reader1": []}, self.library.readers)

    def test_add_reader_with_existing_reader(self):
        self.library.add_reader("Reader1")
        result = self.library.add_reader("Reader1")

        self.assertEqual({"Reader1": []}, self.library.readers)
        self.assertEqual("Reader1 is already registered in the Library library.", result)

    def test_rent_book_if_reader_not_registered(self):
        self.library.add_book("Author1", "Book1")

        result = self.library.rent_book("Reader1", "Author1", "Book1")

        self.assertEqual("Reader1 is not registered in the Library Library.", result)

    def test_rent_book_if_not_book_author_found(self):

        self.library.add_book("Author1", "Book1")
        self.library.add_reader("Reader1")

        result = self.library.rent_book("Reader1", "Author2", "Book1")

        self.assertEqual("Library Library does not have any Author2's books.", result)
        self.assertEqual({"Author1": ["Book1"]}, self.library.books_by_authors)

    def test_rent_book_if_book_title_not_found(self):
        self.library.add_book("Author1", "Book1")
        self.library.add_reader("Reader1")

        result = self.library.rent_book("Reader1", "Author1", "Book2")

        self.assertEqual("""Library Library does not have Author1's "Book2".""", result)

    def test_rent_book_with_valid_data(self):
        self.library.add_book("Author1", "Book1")
        self.library.add_book("Author1", "Book2")
        self.library.add_reader("Reader1")

        self.library.rent_book("Reader1", "Author1", "Book1")

        self.assertEqual({"Reader1": [{"Author1": "Book1"}]}, self.library.readers)
        self.assertEqual({"Author1": ["Book2"]}, self.library.books_by_authors)