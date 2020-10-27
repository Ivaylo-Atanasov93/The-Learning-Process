class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        book_found = [book for book in self.books if book.title == title]
        if len(book_found) > 0:
            return [', '.join([book for book in book_found])]
        return "No matches"


class Reader():
    def __init__(self, name):
        self.name = name
        self.books_taken = []
        self.current_page = None

    def add_book(self, book):
        self.books_taken.append(book)

    def turn_page(self):
        if not self.current_page:
            self.current_page = 1
            return
        self.current_page += 1


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

#--------------Initial Code---------------
# Problem:
# 1.	Books
# Refactor the provided code, so there is a separate class called Library, which contains books and
# has a method called find_book(title) that returns the book with the given title. Remove the unnecessary
# code from the Book class.


# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page
