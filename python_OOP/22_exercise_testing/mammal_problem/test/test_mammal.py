from unittest import TestCase, main

from mammal import Mammal


class MammalTests(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Peter", "Lion", "Roar")

    def test_constructor(self):
        self.assertEqual("Peter", self.mammal.name)
        self.assertEqual("Lion", self.mammal.type)
        self.assertEqual("Roar", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_make_sound(self):
        expected = "Peter makes Roar"
        actual = self.mammal.make_sound()

        self.assertEqual(expected, actual)

    def test_if_return_kingdom(self):
        expected = "animals"
        actual = self.mammal.get_kingdom()

        self.assertEqual(expected, actual)

    def test_if_gets_info(self):
        expected = "Peter is of type Lion"
        actual = self.mammal.info()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
