import json

class Book:
    def __init__(self, title, author, published_year, isbn, genre=None):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.isbn = isbn
        self.genre = genre

    def to_dict(self):
        return self.__dict__

BOOKS = []
