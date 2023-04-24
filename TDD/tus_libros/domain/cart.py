class Cart:
    INVALID_QUANTITY = "Quantity must a strictly positive integer"
    INVALID_PRODUCT = "Invalid product"

    def __init__(self, catalog):
        self._products = list()
        self._catalog = catalog

    def is_empty(self):
        return len(self._products) == 0

    def add(self, product, quantity=1):
        self.assert_is_valid_product(product)
        self.assert_is_valid_quantity(quantity)

        for _ in range(quantity):
            self._products.append(product)

    def assert_is_valid_quantity(self, quantity):
        if quantity < 1 or not isinstance(quantity, int):
            raise Exception(Cart.INVALID_QUANTITY)

    def assert_is_valid_product(self, product):
        if not (product in self._catalog):
            raise Exception(Cart.INVALID_PRODUCT)

    def countOf(self, product):
        return self._products.count(product)

    def get_total_products(self) -> list[str]:
        return len(self._products)