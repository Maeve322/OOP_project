class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = set(products)
        Category.total_categories += 1
        Category.total_unique_products += len(self.products)

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity