class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        try:
            year_int = int(year)
            if year_int < 1886 or year_int > 2100:
                raise ValueError("Рік має бути між 1886 та 2100")
            self.year = year_int
        except (ValueError, TypeError):
            raise ValueError("Рік має бути цілим числом")
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
        return self.__speed

    def brake(self):
        self.__speed = max(0, self.__speed - 5)
        return self.__speed

    def get_speed(self):
        return self.__speed

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


def task03():
    car = Car("BMW", "520i", 2020)
    print(f"Тестуємо автомобіль {car}")
    for _ in range(5):
        car.accelerate()
        print(f"Поточна швидкість: {car.get_speed()} км/год")
    for _ in range(5):
        car.brake()
        print(f"Поточна швидкість: {car.get_speed()} км/год")


task03()

