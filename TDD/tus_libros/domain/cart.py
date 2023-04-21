from abc import ABCMeta
class Cart(metaclass=ABCMeta):
    def __init__(self):
        self._books = []
    def is_empty(self):
        return len(self._books)==0

    def add(self, isbn):
         self._books.append(isbn)