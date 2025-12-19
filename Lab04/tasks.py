import random

def enter_integer_list(text="Введіть цілі числа через пробіл: "):
    while True:
        numbers_input = input(text).split()

        if not numbers_input:
            print("Помилка: ви не ввели жодного числа.")
            continue

        numbers = []
        all_valid = True

        for x in numbers_input:
            try:
                numbers.append(int(x))
            except ValueError:
                print(f"Помилка: '{x}' — не ціле число.")
                all_valid = False

        if all_valid and numbers:
            return numbers
        else:
            print("Спробуйте ще раз.\n")


def valid_list_n_elements(numbers, required_length):
    if numbers is None or not isinstance(numbers, list):
        print("Помилка: передано некоректний список.")
        return False
    if len(numbers) != required_length:
        print(f"Помилка: список має містити рівно {required_length} елементів.")
        return False
    return True


def valid_integers(numbers):
    if not all(isinstance(n, int) for n in numbers):
        print("Є елементи, які не є цілими числами")
        return False
    return True


def task1():
    numbers = enter_integer_list("Введіть цілі числа через пробіл: ")

    maxn = max(numbers)
    print("Найбільший елемент:", maxn)
    numbers.reverse()
    print("Список у зворотному порядку:", numbers)


def task2():
    numbers = enter_integer_list("Введіть цілі числа через пробіл: ")

    positives = [n for n in numbers if n > 0]
    others = [n for n in numbers if n <= 0]

    print("Вихідний список:", numbers)
    print("Додатні числа:", positives)
    print("Інші числа:", others)


def task3(numbers):
    if not valid_list_n_elements(numbers, 20):
        return

    print("Вихідний список:", numbers)

    odd_index_sum = 0
    for i in range(1, len(numbers), 2):
        try:
            odd_index_sum += float(numbers[i])
        except (ValueError, TypeError):
            print(f"Попередження: елемент {numbers[i]} не є числом.")

    print("Сума чисел з непарними індексами:", odd_index_sum)


def task4():
    numbers = [random.randint(-100, 100) for _ in range(30)]
    print("Вихідний список:", numbers)

    max_value = max(numbers)
    max_index = numbers.index(max_value)
    print(f"Максимальний елемент: {max_value}, індекс: {max_index}")

    odd_numbers = [n for n in numbers if n % 2 != 0]

    if odd_numbers:
        odd_numbers.sort(reverse=True)
        print("Непарні числа у порядку зменшення:", odd_numbers)
    else:
        print("Непарних чисел немає.")


def task5():
    numbers = [random.randint(-100, 100) for _ in range(30)]
    print("Вихідний список:", numbers)

    pairs = []
    for i in range(len(numbers) - 1):
        if numbers[i] < 0 and numbers[i + 1] < 0:
            pairs.append((numbers[i], numbers[i + 1]))

    if pairs:
        print("Пари від'ємних чисел, що стоять поруч:", pairs)
    else:
        print("Пар від'ємних чисел, що стоять поруч, не знайдено.")


def task6(numbers):
    if not valid_list_n_elements(numbers, 10):
        return

    if not valid_integers(numbers):
        return

    max_value = max(numbers)

    numbers2 = []
    for num in numbers:
        if num != max_value:
            numbers2.append(pow(num, 2))

    if not numbers2:
        print("Всі елементи рівні максимальному значенню.")
        return

    numbers2.sort(reverse=True)

    print("Вихідний список:", numbers)
    print("Максимальний елемент:", max_value)
    print("Квадрати менших чисел у порядку зменшення:", numbers2)


def task7():
    numbers = []
    for _ in range(30):
        if random.choice([True, False]):
            numbers.append(round(random.randint(-100, 100), 2))
        else:
            numbers.append(round(random.uniform(-100, 100), 2))
    print("Вихідний список:", numbers)

    min_abs_value = min(numbers, key=abs)
    print("Мінімальний за модулем елемент:", min_abs_value)

    sorted_numbers = sorted(numbers)
    print("Список у порядку зростання:", sorted_numbers)


def task8():
    numbers = []
    for _ in range(30):
        if random.choice([True, False]):
            numbers.append(round(random.randint(-100, 100), 2))
        else:
            numbers.append(round(random.uniform(-100, 100), 2))
    print("Вихідний список:", numbers)

    numbers2 = []
    for i in range(0, len(numbers), 3):
        numbers2.append(numbers[i:i + 3])

    sorted_numbers2 = sorted(numbers2, key=lambda sublist: sum(map(abs, sublist)))

    print("Підсписки у порядку зростання за сумою абсолютних значень:")
    for obj in sorted_numbers2:
        print(obj)


def main():
    while True:
        print("Виберіть завдання:")
        print("  1 - Максимальний елемент та зворотній порядок")
        print("  2 - Розділення на додатні та інші елементи")
        print("  3 - Сума елементів з непарними індексами")
        print("  4 - Максимальний елемент та непарні числа")
        print("  5 - Пари від'ємних чисел, що стоять поруч")
        print("  6 - Квадрати менших за максимум")
        print("  7 - Мінімальний по модулю та сортування")
        print("  8 - Формування 10 списків по 3 елементи")
        print("  0 - Вихід")

        choice = input("\nВаш вибір: ").strip()

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            numbers = enter_integer_list("Введіть 20 цілих чисел через пробіл: ")
            task3(numbers)
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '6':
            numbers = enter_integer_list("Введіть 10 цілих чисел через пробіл: ")
            task6(numbers)
        elif choice == '7':
            task7()
        elif choice == '8':
            task8()

        elif choice == '0':
            break
        else:
            print("Ви ввели якусь фігню. Спробуйте ще раз")

if __name__ == "__main__":
    main()