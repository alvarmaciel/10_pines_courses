import unittest
from datetime import date
from domain.cart import Cart



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

    def test_list_purchases(self):
        cart = self.create_cart()
        cart.add(self.valid_product(), 3)
        cart.add(self.another_valid_product(), 2)
        cashier = self.create_cashier()
        self.assertEqual(cashier.list_purchases(cart), 5)

    def test_cashier_know_total_of_prices_in_cart(self):
        cart = self.create_cart()
        cart.add(self.valid_product(), 2)
        cart.add(self.another_valid_product(), 2)
        cashier = self.create_cashier()
        self.assertEqual(cashier.amount_of_cart(cart), 30)

    def test_checkout_implement_list_purchases(self):
        cart = self.create_cart()
        cart.add(self.valid_product(), 2)
        cart.add(self.another_valid_product(), 2)
        cashier = self.create_cashier()
        self.assertEqual(cashier.checkout(cart), True)

    def test_no_checkout_stolen_credit_card(self):
        cart, cashier = self.give_me_a_full_cart_and_a_cashier()
        credit_card = {"number": "1234567890123456", "expiration": "12/2020", "owner": "Juan Perez"}
        with self.assertRaises(Exception) as cm:
            cashier.checkout(cart, credit_card)

        self.assertEqual(cashier.BANNED_CREDIT_CARD, str(cm.exception))

    def test_checkout_not_banned_credit_card(self):
        cart, cashier = self.give_me_a_full_cart_and_a_cashier()
        credit_card = self.give_me_a_valid_credit_card()
        self.assertEqual(cashier.checkout(cart, credit_card), True)
    def test_checkout_not_banned_credit_card_wrong_type_raise_exception(self):
        cart, cashier = self.give_me_a_full_cart_and_a_cashier()
        credit_card = {"number": 1, "expiration": "12/2020", "owner": "Juan Perez"}
        with self.assertRaises(Exception) as cm:
            cashier.checkout(cart, credit_card)

        self.assertEqual(cashier.INVALID_CREDIT_CARD, str(cm.exception))

    def test_checkout_not_banned_credit_card_wrong_len_raise_exception(self):
        cart, cashier = self.give_me_a_full_cart_and_a_cashier()
        credit_card = {"number": "1234567890", "expiration": "12/2020", "owner": "Juan Perez"}
        with self.assertRaises(Exception) as cm:
            cashier.checkout(cart, credit_card)

        self.assertEqual(cashier.INVALID_CREDIT_CARD, str(cm.exception))

    def test_checkout_not_banned_credit_card_wrong_expiration_raise_exception(self):
        cart, cashier = self.give_me_a_full_cart_and_a_cashier()
        exptiration = f"{date.today().month}/{date.today().year - 1}"
        credit_card = {"number": "1234567890123457", "expiration": exptiration, "owner": "Juan Perez"}
        with self.assertRaises(Exception) as cm:
            cashier.checkout(cart, credit_card)

        self.assertEqual(cashier.INVALID_CREDIT_CARD, str(cm.exception))
    def create_catalog(self):
        return {self.valid_product(): 10, self.another_valid_product(): 5}

    def create_cashier(self):
        return Cashier(self.create_catalog())

    def create_cart(self):
        return Cart(self.create_catalog())

    def valid_product(self):
        return "ISBN1"

    def another_valid_product(self):
        return "ISBN2"

    def invalid_product(self):
        return "ISBN3"

    def give_me_a_full_cart_and_a_cashier(self):
        cart = self.create_cart()
        cart.add(self.valid_product(), 2)
        cart.add(self.another_valid_product(), 2)
        cashier = self.create_cashier()
        return cart, cashier
    def give_me_a_valid_credit_card(self):
        month = date.today().month
        year = date.today().year
        return {"number": "1234567890123457", "expiration": f"{month}/{year}", "owner": "Juan Perez"}


if __name__ == '__main__':
    unittest.main()
