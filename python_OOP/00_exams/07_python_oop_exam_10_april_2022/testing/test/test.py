from unittest import TestCase

from project.movie import Movie


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Test", 2000, 5)

    def test_setter_for_name_with_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ve:
            Movie("", 2000, 5)

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_setter_for_year_with_invalid_data_raises(self):
        with self.assertRaises(ValueError) as ve:
            Movie("Test", 1886, 5)

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_adding_actor_that_already_exists(self):
        # TODO if only adding actor who doesnt exist
        self.movie.add_actor("Gosho")
        actual_result = self.movie.add_actor("Gosho")

        self.assertEqual("Gosho is already added in the list of actors!", actual_result)
        self.assertEqual(["Gosho"], self.movie.actors)

    def test_greater_than_method_with_self_greater(self):
        other_movie = Movie("Test1", 2000, 4)
        result = self.movie > other_movie
        self.assertEqual('"Test" is better than "Test1"', result)

    def test_greater_than_method_with_equal(self):
        other_movie = Movie("Test1", 2000, 5)
        result = self.movie < other_movie
        self.assertEqual('"Test" is better than "Test1"', result)

    def test_greater_than_method_with_equal_new(self):
        other_movie = Movie("Test1", 2000, 5)
        result = self.movie > other_movie
        self.assertEqual('"Test1" is better than "Test"', result)

    def test_repr_method(self):
        self.movie.add_actor("Ivan")
        self.movie.add_actor("Stoyan")

        expected_result = "Name: Test\n" \
                          "Year of Release: 2000\n" \
                          "Rating: 5.00\n" \
                          "Cast: Ivan, Stoyan"

        self.assertEqual(expected_result, repr(self.movie))