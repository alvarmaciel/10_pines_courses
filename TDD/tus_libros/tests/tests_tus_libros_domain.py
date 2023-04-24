import unittest

from TDD.tus_libros.domain.cart import Cart
from TDD.tus_libros.domain.cashier import Cashier


class ShoppingTest(unittest.TestCase):
    def test_cart_is_created_empty(self):
        self.assertTrue(self.create_cart().is_empty())

    def test_cart_is_not_empty_when_adding_products(self):
        cart = self.create_cart()
        cart.add(self.valid_product())

        self.assertFalse(cart.is_empty())

    def test_can_not_add_products_not_sell(self):
        cart = self.create_cart()

        with self.assertRaises(Exception) as cm:
            cart.add(self.invalid_product())

        self.assertEqual(Cart.INVALID_PRODUCT, str(cm.exception))
        self.assertTrue(cart.is_empty())

    def test_can_add_many_products_at_once(self):
        cart = self.create_cart()

        cart.add(self.valid_product(), 2)

        self.assertEqual(2, cart.countOf(self.valid_product()))

    def test_can_add_many_different_products_at_once(self):
        cart = self.create_cart()

        cart.add(self.valid_product(), 2)
        cart.add(self.another_valid_product(), 1)

        self.assertEqual(2, cart.countOf(self.valid_product()))
        self.assertEqual(1, cart.countOf(self.another_valid_product()))

    def test_quantity_to_add_must_be_strictly_positive(self):
        cart = self.create_cart()

        with self.assertRaises(Exception) as cm:
            cart.add(self.valid_product(), 0)

        self.assertEqual(Cart.INVALID_QUANTITY, str(cm.exception))
        self.assertTrue(cart.is_empty())

    def test_quantity_to_add_must_be_integer(self):
        cart = self.create_cart()

        with self.assertRaises(Exception) as cm:
            cart.add(self.valid_product(), 1.1)

        self.assertEqual(Cart.INVALID_QUANTITY, str(cm.exception))
        self.assertTrue(cart.is_empty())

    def test_no_checkout_of_empty_cart(self):
        cart = self.create_cart()
        cashier = self.create_cashier()
        with self.assertRaises(Exception) as cm:
            cashier.checkout(cart)

        self.assertEqual(cashier.EMPTY_CART, str(cm.exception))
        self.assertEqual(cashier.list_purchases(cart), 0)

    def test_checkout_non_empty_cart_list_purchases(self):
        cart = self.create_cart()
        cart.add(self.valid_product(), 3)
        cart.add(self.another_valid_product(), 2)
        cashier = self.create_cashier()
        cashier.checkout(cart)
        self.assertEqual(cashier.list_purchases(cart), 5)

    def test_total_of_prices_in_cart(self):
        cart = self.create_cart()
        cart.add(self.valid_product(), 2)
        cart.add(self.another_valid_product(), 2)
        cashier = self.create_cashier()
        self.assertEqual(cashier.amount_of_cart(cart), 30)
    def create_cashier(self):
        return Cashier({self.valid_product(): 10, self.another_valid_product():5})
    def create_cart(self):
        return Cart({self.valid_product(): 10, self.another_valid_product():5})

    def valid_product(self):
        return "ISBN1"

    def another_valid_product(self):
        return "ISBN2"

    def invalid_product(self):
        return "ISBN3"


if __name__ == '__main__':
    unittest.main()