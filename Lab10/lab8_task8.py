class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        if not shop_name or not isinstance(shop_name, str) or not shop_name.strip():
            self.valid = False
            self.shop_name = None
            self.store_type = None
            self.number_of_units = 0
            return
        
        if not store_type or not isinstance(store_type, str) or not store_type.strip():
            self.valid = False
            self.shop_name = None
            self.store_type = None
            self.number_of_units = 0
            return
        
        self.valid = True
        self.shop_name = shop_name.strip()
        self.store_type = store_type.strip()
        self.number_of_units = number_of_units

    def describe_shop(self):
        if not self.valid:
            return None
        return f"Назва магазину: {self.shop_name}\nТип магазину: {self.store_type}"

    def open_shop(self):
        if not self.valid:
            return None
        return f"Магазин '{self.shop_name}' відкритий!"

    def set_number_of_units(self, number):
        if not self.valid:
            return "Помилка: магазин невалідний"
        
        if not isinstance(number, int) or number < 0:
            return "Помилка: кількість видів товару має бути додатнім цілим числом"
        
        self.number_of_units = number
        return None

    def increment_number_of_units(self, increment):
        if not self.valid:
            return "Помилка: магазин невалідний"
        
        if not isinstance(increment, int) or increment < 0:
            return "Помилка: збільшення кількості має бути додатнім цілим числом"
        
        self.number_of_units += increment
        return None


class Discount(Shop):
    def __init__(self, shop_name, store_type, number_of_units=0, discount_products=None):
        super().__init__(shop_name, store_type, number_of_units)
        
        if discount_products is None:
            discount_products = []
        
        if not isinstance(discount_products, list):
            self.valid = False
            self.discount_products = []
            return
        
        for product in discount_products:
            if not isinstance(product, str) or not product.strip():
                self.valid = False
                self.discount_products = []
                return
        
        self.discount_products = [p.strip() for p in discount_products if p.strip()]

    def get_discounts_products(self):
        if not self.valid:
            return None
        
        if not self.discount_products:
            return "Список товарів зі знижками порожній"
        
        products_list = "\n".join([f"- {product}" for product in self.discount_products])
        return f"Товари зі знижками:\n{products_list}"

    def add_discount_product(self, product):
        if self.valid and product not in self.discount_products:
            self.discount_products.append(product)