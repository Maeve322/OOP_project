class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str,products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.total_categories += 1
        Category.total_unique_products += len(set(self.__products))
    def add(self,product):
        self.__products.append(product)
    def get_products(self):
        return self.__products

    def __len__(self):
        return sum(product.quantity for product in self.__products)

    
    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, **product_data):
        return cls(**product_data)

    @staticmethod
    def create_product(name, description, price, quantity, existing_products):
        for product in existing_products:
            if product.name == name:
                if product.price < price:
                    product.price = price
                product.quantity += quantity
                return product
        # Если продукт с таким именем не найден, создаем новый продукт
        new_product_data = {
            'name': name,
            'description': description,
            'price': price,
            'quantity': quantity
        }
        new_product = Product.new_product(**new_product_data)
        return new_product

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,new_price):
        if new_price <= 0:
            print("Цена введена некорректно. Цена должна быть больше нуля.")
        elif new_price < self.price:
            discount_answer = input("Вы точно хотите снизить цену? (y/n)")
            if discount_answer == 'y':
                self.__price = new_price
        else:
            self.__price = new_price

 # Название продукта, 80 руб. Остаток: 15 шт.
    
    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"


    def __add__(self, other):
        return (self.price*self.quantity) + (other.price * other.quantity)




    
class inspectionsCategory:
    def __init__(self, category):
        self.category = category
        self.products = self.category.get_products()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
        
        
