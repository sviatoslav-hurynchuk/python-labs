class Buffer:
    MAX_SIZE = 1000000
    
    def __init__(self):
        self.__elements = []

    def add(self, *a):
        for item in a:
            if not isinstance(item, (int, float)):
                raise TypeError("Всі елементи мають бути числами")

        if len(self.__elements) + len(a) > self.MAX_SIZE:
            raise ValueError(f"Буфер переповнений. Максимальний розмір: {self.MAX_SIZE}")
        self.__elements.extend(a)
        while len(self.__elements) >= 5:
            sum_of_five = sum(self.__elements[:5])
            print(sum_of_five)
            self.__elements = self.__elements[5:]

    def get_current_part(self):
        return self.__elements


def task05():
    buf = Buffer()
    buf.add(1, 2, 3)
    print(f"Поточна частина: {buf.get_current_part()}")
    buf.add(4, 5, 6)
    print(f"Поточна частина: {buf.get_current_part()}")
    buf.add(7, 8, 9, 10, 11, 12, 13)
    print(f"Поточна частина: {buf.get_current_part()}")


task05()

