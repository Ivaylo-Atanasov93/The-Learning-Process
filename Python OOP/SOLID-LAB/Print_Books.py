class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book, formatter: Formatter):
        formatter = formatter
        formatted_book = formatter.format(book)
        return formatted_book

#--------------Initial Code---------------
# Problem:
# 5.	Print books
# We want to be able to print books, but before printing the book we should
# be able to format it. To accomplish this we have a class that can print
# books called Printer and a class Formatter which is used by Printer.
# Refactor the provided code that breaks the DIP because both Printer and
# Formatter depend on concretions, not abstractions by creating some abstractions
# and inject them wherever they are needed.
# class Book:
#     def __init__(self, content: str):
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book
