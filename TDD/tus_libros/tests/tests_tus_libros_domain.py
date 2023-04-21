import unittest
from domain.cart import Cart



class MyTestCase(unittest.TestCase):
    def test_un_carro_nuevo_es_vacio(self):
        self.assertTrue(Cart().is_empty())  # add assertion here

    def test_agrega_un_libro_y_no_es_vacio(self):
        isbn = 1
        cart = Cart()
        cart.add(isbn)
        self.assertFalse(cart.is_empty())

if __name__ == '__main__':
    unittest.main()
