class Bank:
    def __init__(self, balance):
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Початковий баланс має бути додатнім числом")
        if balance > 1e15: 
            raise ValueError("Баланс занадто великий")

        from decimal import Decimal
        self.__balance = Decimal(str(balance))

    @staticmethod
    def __validate_amount(amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума операції має бути додатнім числом")
        if amount > 1e15:
            raise ValueError("Сума операції занадто велика")
            
        from decimal import Decimal
        return Decimal(str(amount))

    def deposit(self, amount):
        amount = self.__validate_amount(amount)
        self.__balance += amount
        return float(self.__balance)

    def withdraw(self, amount):
        amount = self.__validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.__balance -= amount
        return float(self.__balance)

    def get_balance(self):
        return round(float(self.__balance), 2)


def task01():
    bank_account = Bank(1500)
    bank_account.deposit(350.75)
    try:
        bank_account.withdraw(2000)
    except ValueError as error:
        print(f"{error}")
    bank_account.withdraw(250)
    print(f"Поточний баланс: {bank_account.get_balance()} грн")


task01()

