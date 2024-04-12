import pytest
from OOP_begin import Category,Product


@pytest.fixture
def category_instance():
    category = Category("Electronics", "Category for electronic products")
    return category

@pytest.fixture
def product_instance():
    product = Product("Laptop", "High-performance laptop", 1200, 10)
    return product



def test_category_initialization(category_instance):
    assert category_instance.name == "Electronics"
    assert category_instance.description == "Category for electronic products"
    assert len(category_instance.products) == 0

def test_product_initialization(product_instance):
    assert product_instance.name == "Laptop"
    assert product_instance.description == "High-performance laptop"
    assert product_instance.price == 1200
    assert product_instance.quantity == 10


def test_total_categories():
    assert Category.total_categories == 1

def test_total_unique_products():
    assert Category.total_unique_products == 1



# Запуск тестов
if __name__ == "__main__":
    pytest.main()