from test.project import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {} #the AUTHORS (key: str) and the BOOKS AVAILABLE for each of the authors (list of strings)
        self.rented_books = {} #the USERNAMES (key: str) and nested dictionary with the BOOK NAMES (key: str) and DAYS

    def get_book(self, author, book_name, days_to_return, user: User):
        if book_name in self.books_available[author]:
            try:
                self.rented_books[user.username][book_name] = days_to_return
            except KeyError:
                self.rented_books[user.username] = {book_name: days_to_return}

            self.books_available[author].remove(book_name)
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        return f'The book "{book_name}" is already rented and will be available in ' \
               f'{self.rented_books[user.username][book_name]} days!'

    def return_book(self, author, book_name, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
        user.books.remove(book_name)
