from abc import ABC, abstractmethod


class Animal(ABC):

    @staticmethod
    @abstractmethod
    def make_sound():
        pass


class Cat(Animal):
    @staticmethod
    def make_sound():
        return 'meow'


class Dog(Animal):
    @staticmethod
    def make_sound():
        return 'woof-woof'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
