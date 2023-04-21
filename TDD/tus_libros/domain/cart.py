from datetime import datetime, timedelta

class Cart:
    def __init__(self):
        self._books = []
        self._created_at = datetime.utcnow()
    def is_empty(self):
        delta = timedelta(minutes=30)
        if self._created_at + delta <= datetime.utcnow():
            self._books.clear()
        return len(self._books) == 0

    def add(self, isbn: str):
        self._books.append(isbn)