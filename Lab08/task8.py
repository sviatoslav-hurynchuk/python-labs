from shop import Shop, Discount


def task08a():
    store = Shop("TechStore", "Електроніка")
    
    print(f"Назва магазину: {store.shop_name}")
    print(f"Тип магазину: {store.store_type}")
    store.describe_shop()
    store.open_shop()


def task08b():
    store1 = Shop("FashionStore", "Одяг")
    store2 = Shop("BookStore", "Книги")
    store3 = Shop("FoodStore", "Продукти")
    
    store1.describe_shop()
    store2.describe_shop()
    store3.describe_shop()


def task08c():
    store = Shop("TechStore", "Електроніка")
    print(f"Кількість видів товару: {store.number_of_units}")
    
    store.number_of_units = 50
    print(f"Кількість видів товару (після зміни): {store.number_of_units}")


def task08d():
    store = Shop("TechStore", "Електроніка")
    
    store.set_number_of_units(100)
    print(f"Кількість видів товару (після set_number_of_units): {store.number_of_units}")
    
    store.increment_number_of_units(25)
    print(f"Кількість видів товару (після increment_number_of_units): {store.number_of_units}")


def task08e():
    store_discount = Discount("SuperMarket", "Супермаркет")
    store_discount.add_discount_product("Молоко")
    store_discount.add_discount_product("Хліб")
    store_discount.add_discount_product("Яблука")
    
    discounts = store_discount.get_discounts_products()
    print(f"Товари зі знижкою: {discounts}")


def task08f():
    all_store = Shop("AllStore", "Універсальний магазин", 200)
    all_store.describe_shop()
    all_store.open_shop()


def task08():
    task08a()
    task08b()
    task08c()
    task08d()
    task08e()
    task08f()


task08()

