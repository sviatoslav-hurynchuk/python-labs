class Human:
    default_name = "Unknown"
    default_age = 0

    def __init__(self, name=None, age=None, money=0, house=None):
        if name is None:
            name = Human.default_name
        if age is None:
            age = Human.default_age

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я має бути непорожнім рядком")
        if not isinstance(age, (int, float)) or age < 0:
            raise ValueError("Вік має бути невід'ємним числом")
        if not isinstance(money, (int, float)) or money < 0:
            raise ValueError("Гроші мають бути невід'ємним числом")
        if house is not None and not isinstance(house, House):
            raise TypeError("house має бути екземпляром класу House або None")

        self.name = name.strip()
        self.age = age
        self.__money = float(money)
        self.__house = house

    def info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Будинок: {self.__house}")
        print(f"Гроші: {self.__money}")

    @staticmethod
    def default_info():
        print(f"Ім'я за замовчуванням: {Human.default_name}")
        print(f"Вік за замовчуванням: {Human.default_age}")

    def __make_deal(self, house, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Ціна має бути невід'ємним числом")
        if self.__money < price:
            raise ValueError("Недостатньо грошей для угоди")
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума заробітку має бути додатнім числом")
        self.__money += amount

    def buy_house(self, house, discount=10):
        if not isinstance(house, House):
            print("Помилка: об'єкт будинку має бути типу House")
            return False
        if not isinstance(discount, (int, float)):
            print("Помилка: знижка має бути числом")
            return False
        if discount < 0 or discount > 100:
            print("Попередження: знижка має бути в діапазоні 0-100%. Значення буде обмежено цими межами.")
            discount = max(0, min(100, discount))

        if self.__house is not None:
            print(f"Попередження: У вас вже є будинок!")
            return False

        final_price = house.final_price(discount)
        if self.__money < final_price:
            print(f"Попередження: Недостатньо грошей! У вас {self.__money}, а потрібно {final_price}")
            return False

        self.__make_deal(house, final_price)
        print(f"Будинок успішно куплено! Залишок грошей: {self.__money}")
        return True


class House:
    def __init__(self, area=100, price=100000):
        if not isinstance(area, (int, float)) or area <= 0:
            raise ValueError("Площа будинку має бути додатнім числом")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Ціна будинку має бути додатнім числом")
        self._area = float(area)
        self._price = float(price)

    def final_price(self, discount):
        if not isinstance(discount, (int, float)):
            raise ValueError("Знижка має бути числом")
        discount = max(0, min(100, discount))
        return round(self._price * (1 - discount / 100))


class SmallHouse(House):
    def __init__(self, price=100000):
        super().__init__(area=40, price=price)


def task02():
    print("Довідкова інформація")
    Human.default_info()
    print()

    print("Створення об'єкта Human")
    human = Human("Іван", 25)
    human.info()
    print()

    print("Створення об'єкта SmallHouse")
    small_house = SmallHouse(price=50000)
    print(f"Площа SmallHouse: {small_house._area} м², ціна: {small_house._price}")
    print()

    print("Спроба купити будинок (має не вдатися)")
    human.buy_house(small_house)
    print()

    print("Збільшення грошей")
    human.earn_money(60000)
    human.info()
    print()

    print("Спроба купити будинок знову (має вдатися)")
    human.buy_house(small_house)
    print()

    print("Фінальний стан об'єкта Human")
    human.info()

task02()