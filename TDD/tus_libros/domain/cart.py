from abc import ABCMeta
from datetime import datetime


class Cart(metaclass=ABCMeta):
    def __init__(self):
        self._books = []
        self._created_at = datetime.utcnow()
    def is_empty(self):
        return len(self._books)==0

    def add(self, isbn: str):
        self._books.append(isbn)