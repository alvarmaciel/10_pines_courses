from datetime import date

from .cart import Cart
from typing import Dict


class Cashier:
    EMPTY_CART = "There is no product for checkout"
    BANNED_CREDIT_CARD = "Banned credit card"
    INVALID_CREDIT_CARD = "Invalid credit card"

    def __init__(self, catalog):
        self._catalog = catalog
        self._banned_credit_cards = ["1234567890123456"]

    def checkout(self, cart: Cart, credit_card: Dict[str, str] = None) -> bool:
        if cart.is_empty():
            raise Exception(self.EMPTY_CART)
        if credit_card and credit_card["number"] in self._banned_credit_cards:
            raise Exception(self.BANNED_CREDIT_CARD)
        list_purchased = self.list_purchases(cart)
        verified_credit_card: bool = self._verified_credit_card(credit_card) if credit_card else True
        return list_purchased > 0 and verified_credit_card is True

    def list_purchases(self, cart: Cart):
        return cart.get_total_products()

    def amount_of_cart(self, cart) -> int:
        amount = 0
        for product in cart.get_all_products():
            amount += self._catalog[product]
        return amount

    def _verified_credit_card(self, credit_card: Dict[str, str]) -> bool:
        today = date(date.today().year, date.today().month, 1)
        expiration = credit_card["expiration"].split("/")
        expiration_date = date(int(expiration[1]), int(expiration[0]), 1)
        if type(credit_card["number"]) is not str:
            raise Exception(self.INVALID_CREDIT_CARD)
        elif len(credit_card["number"]) != 16:
            raise Exception(self.INVALID_CREDIT_CARD)
        elif expiration_date < today:
            raise Exception(self.INVALID_CREDIT_CARD)
        else:
            return True
