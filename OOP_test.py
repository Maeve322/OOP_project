import pytest
from unittest.mock import patch
from OOP_begin import Category,Product




@pytest.fixture
def create_product():
    product = Product("Laptop", "High-performance laptop", 1000.0, 10)
    return product

@pytest.fixture
def create_category():
    product = Product("Laptop","High-performance laptop", 1000.0, 10)
    category = Category("Electronics", "Category for electronic products", [product])
    return category

def test_category_init(create_category):
    assert create_category.name == "Electronics"
    assert create_category.description == "Category for electronic products"
    assert len(create_category._Category__products) == 1


def test_product_init(create_product):
    assert create_product.name == "Laptop"
    assert create_product.description == "High-performance laptop"
    assert create_product.price == 1000.0
    assert create_product.quantity == 10

def test_add_product_to_category(create_category, create_product):
    create_category.add(create_product)
    assert len(create_category._Category__products) == 2

def test_products_count(create_category):
    assert len(create_category) == 10
    
def test_category_get_products(create_category):
    products = create_category.get_products()
    assert products[0].name == "Laptop"
def test_products_info(create_category):
    product_info = str(create_category)
    assert "Electronics, количество продуктов: 10 шт." == product_info

def test_category_length(create_category,create_product):
    create_category.add(create_product)
    assert len(create_category) == 20
def test_create_product(create_product):
    existing_product = [Product("Laptop","High-performance laptop",1000.0,10)]
    new_product = Product.create_product("Laptop","High-performance laptop",1500.0,10,existing_product)
    assert new_product.price == 1500.0
    assert new_product.quantity == 20

def test_product_price_s(create_product):
    assert create_product.price == 1000

    create_product.price = 2200
    assert create_product.price == 2200

    with patch('builtins.input', return_value='n'):
        create_product.price = 50
        assert create_product.price == 2200

    with patch('builtins.input', return_value='y'):
        create_product.price = 40
        assert create_product.price == 40


def test_product_info(create_product):
    assert "Laptop, 1000.0 руб. Остаток: 10 шт.\n" == str(create_product)

def test_product_add(create_product):
    summary = create_product + Product("Laptop","High-performance laptop",1000.0,10)
    assert summary == 20000.0


# Проверка работоспособности интерфейса InspectionsCategory
def test_inspections_category_init(create_category):
    assert create_category.name == "Electronics"
    assert create_category.description == "Category for electronic products"
    assert len(create_category._Category__products) == 1
# Запуск тестов
if __name__ == "__main__":
    pytest.main()