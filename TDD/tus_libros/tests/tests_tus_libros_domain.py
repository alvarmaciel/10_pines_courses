import unittest

from datetime import timedelta
from freezegun import freeze_time

from domain.cart import Cart


class CartTestCase(unittest.TestCase):
    def test_un_carro_nuevo_es_vacio(self):
        self.assertTrue(Cart().is_empty())  # add assertion here

    def test_agrega_un_libro_y_no_es_vacio(self):
        isbn = "1"
        cart = Cart()
        cart.add(isbn)
        self.assertFalse(cart.is_empty())

    def test_agregas_mas_de_un_libro(self):
        a_isbn = "1"
        another_isbn = "1a"
        cart = Cart()
        cart.add(a_isbn)
        cart.add(another_isbn)
        self.assertFalse(cart.is_empty())
        self.assertEqual(len(cart._books), 2)

    def test_a_cart_with_books_gets_empty_after_30_minutes_of_creation(self):
        a_isbn = "1"
        another_isbn = "1a"
        cart = Cart()
        cart.add(a_isbn)
        cart.add(another_isbn)
        delta = timedelta(minutes=30)
        created_at = cart._created_at
        with freeze_time((created_at + delta)):
            self.assertTrue(cart.is_empty())

    def test_a_cart_with_books_not_empty_after_29_minutes_of_creation(self):
        a_isbn = "1"
        another_isbn = "1a"
        cart = Cart()
        cart.add(a_isbn)
        cart.add(another_isbn)
        delta = timedelta(minutes=29)
        created_at = cart._created_at
        with freeze_time((created_at + delta)):
            self.assertFalse(cart.is_empty())


if __name__ == '__main__':
    unittest.main()
