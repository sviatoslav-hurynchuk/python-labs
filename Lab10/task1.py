from lab8_task8 import Shop, Discount


class TestShop:
    def test_task08a_create_instance_and_attributes(self):
        store = Shop("TechStore", "Електроніка")
        
        assert store.shop_name == "TechStore"
        assert store.store_type == "Електроніка"
    
    def test_task08a_describe_shop(self):
        store = Shop("TechStore", "Електроніка")
        desc = store.describe_shop()
        
        assert "TechStore" in desc
        assert "Електроніка" in desc
    
    def test_task08a_open_shop(self):
        store = Shop("TechStore", "Електроніка")
        msg = store.open_shop()
        
        assert "відкритий" in msg.lower()
        assert "TechStore" in msg
    
    def test_task08b_three_different_instances(self):
        store1 = Shop("FashionStore", "Одяг")
        store2 = Shop("BookStore", "Книги")
        store3 = Shop("FoodStore", "Продукти")
        
        assert store1.shop_name == "FashionStore"
        assert store1.store_type == "Одяг"
        
        assert store2.shop_name == "BookStore"
        assert store2.store_type == "Книги"
        
        assert store3.shop_name == "FoodStore"
        assert store3.store_type == "Продукти"
        
        desc1 = store1.describe_shop()
        desc2 = store2.describe_shop()
        desc3 = store3.describe_shop()
        
        assert "FashionStore" in desc1
        assert "BookStore" in desc2
        assert "FoodStore" in desc3
    
    def test_task08c_number_of_units_default(self):
        store = Shop("TechStore", "Електроніка")
        assert store.number_of_units == 0
    
    def test_task08c_number_of_units_change(self):
        store = Shop("TechStore", "Електроніка")
        
        assert store.number_of_units == 0
        
        store.number_of_units = 50
        assert store.number_of_units == 50
    
    def test_task08d_set_number_of_units(self):
        store = Shop("TechStore", "Електроніка")
        
        err = store.set_number_of_units(100)
        assert err is None
        assert store.number_of_units == 100
    
    def test_task08d_increment_number_of_units(self):
        store = Shop("TechStore", "Електроніка")
        store.set_number_of_units(100)
        
        err = store.increment_number_of_units(25)
        assert err is None
        assert store.number_of_units == 125
    
    def test_task08f_import(self):
        all_store = Shop("AllStore", "Універсальний магазин", 200)
        
        assert all_store.shop_name == "AllStore"
        assert all_store.store_type == "Універсальний магазин"
        assert all_store.number_of_units == 200
    
    def test_task08f_methods_after_import(self):
        all_store = Shop("AllStore", "Універсальний магазин", 200)
        
        desc = all_store.describe_shop()
        assert "AllStore" in desc


class TestDiscount:
    def test_task08e_inheritance(self):
        store_discount = Discount("SuperMarket", "Супермаркет")
        assert isinstance(store_discount, Shop)
        assert store_discount.shop_name == "SuperMarket"
        assert store_discount.store_type == "Супермаркет"
    
    def test_task08e_discount_products_attribute(self):
        store_discount = Discount("SuperMarket", "Супермаркет")
        assert hasattr(store_discount, 'discount_products')
        assert isinstance(store_discount.discount_products, list)
    
    def test_task08e_get_discounts_products_method(self):
        store_discount = Discount("SuperMarket", "Супермаркет")
        
        store_discount.add_discount_product("Молоко")
        store_discount.add_discount_product("Хліб")
        store_discount.add_discount_product("Яблука")
        
        result = store_discount.get_discounts_products()
        
        assert result is not None
        assert "Молоко" in result
        assert "Хліб" in result
        assert "Яблука" in result

def task01():
    import pytest
    pytest.main([__file__, '-v'])


task01()