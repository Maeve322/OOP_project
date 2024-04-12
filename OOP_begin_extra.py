import json
from OOP_begin import Category,Product

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    categories = []
    products = []

    for category_data in data:
        category = Category(category_data['name'], category_data['description'])
        for product_data in category_data['products']:
            product = Product(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])
            category.products.append(product)
            products.append(product)

        categories.append(category)
    return categories, products

# Пример использования функции
categories, products = load_data_from_json("products.json")

# Вывод информации о категориях и товарах
for category in categories:
    print(f"Category: {category.name} - {category.description}")
    for product in category.products:
        print(f"Product: {product.name} - Price: {product.price} - Quantity: {product.quantity}")

print(f"Total Categories: {Category.total_categories}")
print(f"Total Unique Products: {Category.total_unique_products}")