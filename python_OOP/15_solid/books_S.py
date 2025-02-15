class Book:
    def __init__(self, title, author ):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)

    def remove_book(self, title):
        try:
            searched_book = [x for x in self.books if x.title == title][0]
            self.books.remove(searched_book)
        except IndexError:
            return f"Book {title} not found"

    def find_book(self, title):
        try:
            return [x for x in self.books if x.title == title][0]
        except IndexError:
            return f"Book {title} not found"