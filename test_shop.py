import pytest
from unittest.mock import patch
from shop import Category,Product,inspectionsCategory,Smartphone,Grass




@pytest.fixture
def create_product():
    product = Product("Laptop", "High-performance laptop", 1000.0, 10)
    return product

@pytest.fixture
def create_smartphone_product():
    product = Smartphone("Laptop", "High-performance laptop", 1000.0, 10, "Apple", "Air 15", 4, "White")
    return product

@pytest.fixture
def create_grass_product():
    product = Grass("Laptop", "High-performance laptop", 1000.0, 10, "Russia", 2019, "White")
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

def test_smartphone_init(create_smartphone_product):
    assert create_smartphone_product.name == "Laptop"
    assert create_smartphone_product.description == "High-performance laptop"
    assert create_smartphone_product.price == 1000.0
    assert create_smartphone_product.quantity == 10
    assert create_smartphone_product.company == "Apple"
    assert create_smartphone_product.model == "Air 15"
    assert create_smartphone_product.ram == 4
    assert create_smartphone_product.color == "White"
    assert isinstance(create_smartphone_product,Product) == True
    
def test_grass_init(create_grass_product):
    assert create_grass_product.name == "Laptop"
    assert create_grass_product.description == "High-performance laptop"
    assert create_grass_product.price == 1000.0
    assert create_grass_product.quantity == 10
    assert create_grass_product.country == "Russia"
    assert create_grass_product.date_grown == 2019
    assert create_grass_product.color == "White"
    assert isinstance(create_grass_product,Product) == True
                      
                      
def test_add_product_to_category(create_category, create_product):
    create_category.add(create_product)
    assert len(create_category._Category__products) == 2

def test_category_add_invalid_product(create_category):
    invalid_product = {"Laptop", "High-performance laptop", 1000.0, 10}
    with pytest.raises(TypeError):
        create_category.add(invalid_product)
        
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
def test_product_add_invalid_product(create_smartphone_product,create_grass_product):
    with pytest.raises(TypeError):
        create_smartphone_product + create_grass_product


# Проверка работоспособности интерфейса InspectionsCategory
def test_inspections_category_init(create_category):
    product1 = Product("Laptop", "High-performance laptop", 1000.0, 10)
    product2 = Product("Smartphone", "Flagship smartphone", 800.0, 15)
    category = Category("Electronics", "Category for electronic products", [product1, product2])
    inspection = inspectionsCategory(category)
    products = list(inspection)
    assert len(products) == 2
    assert products[0] == product1
    assert products[1] == product2
    
# Запуск тестов
if __name__ == "__main__":
    pytest.main()