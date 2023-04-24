from .cart import Cart
class Cashier:
    EMPTY_CART = "There is no product for checkout"
    def __init__(self, catalog):
        self._catalog = catalog
    def checkout(self, cart:Cart)-> bool:
        if cart.is_empty():
            raise Exception(self.EMPTY_CART)
        return True

    def list_purchases(self, cart:Cart):
        return cart.get_total_products()

    def amount_of_cart(self, cart) -> int:
        amount = 0
        for product in cart.get_all_products():
            amount += self._catalog[product]
        return amount


