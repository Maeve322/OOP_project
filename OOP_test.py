import pytest
from OOP_begin import Category,Product

@pytest.fixture
def sample_category():
    return Category("Electronics", "Category for electronic products", ["Laptop", "Phone", "Tablet"])

@pytest.fixture
def sample_product():
    return Product("Laptop", "High-performance laptop", 1500.0, 10)

def test_category_initialization(sample_category):
    assert sample_category.name == "Electronics"
    assert sample_category.description == "Category for electronic products"
    assert sample_category.products == {"Laptop", "Phone", "Tablet"}
    assert Category.total_categories == 1
    assert Category.total_unique_products == 3

def test_product_initialization(sample_product):
    assert sample_product.name == "Laptop"
    assert sample_product.description == "High-performance laptop"
    assert sample_product.price == 1500.0
    assert sample_product.quantity == 10

# Запуск тестов
if __name__ == "__main__":
    pytest.main()