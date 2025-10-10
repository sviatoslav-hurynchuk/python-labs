import random

def task1():
    numbers = [random.randint(0, 100) for _ in range(10)]
    print("Вхідні числа:", numbers)
    first_half = [x for x in numbers if x <= 50]
    print("Числа <=50:", first_half)

def task2():
    while True:
        total_input = input("Введіть суму покупки: ")
        if total_input.replace('.', '', 1).isdigit():
            total = float(total_input)
            if total >= 0:
                break
    discount = 0
    if total > 1000:
        discount = 0.05
    elif total > 500:
        discount = 0.03
    final_price = total * (1 - discount)
    print(f"Сума до оплати з урахуванням знижки: {final_price:.2f} грн")

def task4():
    while True:
        a_input = input("Введіть число A: ")
        b_input = input("Введіть число B (B > A): ")
        if a_input.lstrip('-').isdigit() and b_input.lstrip('-').isdigit():
            A = int(a_input)
            B = int(b_input)
            if B > A:
                break
    total_sum = 0
    for i in range(A, B + 1):
        total_sum += i
    print(f"Сума чисел від {A} до {B}:", total_sum)


def task5():
    while True:
        a_input = input("Введіть число A: ")
        b_input = input("Введіть число B (B > A): ")
        if a_input.lstrip('-').isdigit() and b_input.lstrip('-').isdigit():
            A = int(a_input)
            B = int(b_input)
            if B > A:
                break
    sum_squares = 0
    for i in range(A, B + 1):
        sum_squares += i ** 2
    print(f"Сума квадратів чисел від {A} до {B}:", sum_squares)


def task8():
    while True:
        n_input = input("Введіть число N (>1): ")
        if n_input.isdigit():
            N = int(n_input)
            if N > 1:
                break
    K = 0
    while 5**K <= N:
        K += 1
    print(f"Найменше K, для якого 5^K > N: {K}")

def task9():
    while True:
        n_input = input("Введіть число n: ")
        if n_input.lstrip('-').isdigit():
            n = int(n_input)
            break
    for i in range(1, n + 2):
        square = i ** 2
        if square > n:
            print(f"Перше число у послідовності квадратів, більше {n}: {square}")
            break


def task10():
    while True:
        n_input = input("Введіть число n: ")
        if n_input.lstrip('-').isdigit():
            n = int(n_input)
            break
    i = 0
    seq = []
    while True:
        if i == 0:
            num = 1
        else:
            num = seq[-1] + i * 2 - 1
        seq.append(num)
        if num > n:
            print(f"Перше число послідовності, більше {n}: {num}")
            break
        i += 1

def task11():
    while True:
        d_input = input("Введіть день: ")
        m_input = input("Введіть місяць: ")
        if d_input.isdigit() and m_input.isdigit():
            D = int(d_input)
            M = int(m_input)
            if 1 <= M <= 12 and 1 <= D <= 31:
                break
    zodiac = ""
    if (M == 1 and D >= 20) or (M == 2 and D <= 18):
        zodiac = "Водолій"
    elif (M == 2 and D >= 19) or (M == 3 and D <= 20):
        zodiac = "Риби"
    elif (M == 3 and D >= 21) or (M == 4 and D <= 19):
        zodiac = "Овен"
    elif (M == 4 and D >= 20) or (M == 5 and D <= 20):
        zodiac = "Телець"
    elif (M == 5 and D >= 21) or (M == 6 and D <= 21):
        zodiac = "Близнюки"
    elif (M == 6 and D >= 22) or (M == 7 and D <= 22):
        zodiac = "Рак"
    elif (M == 7 and D >= 23) or (M == 8 and D <= 22):
        zodiac = "Лев"
    elif (M == 8 and D >= 23) or (M == 9 and D <= 22):
        zodiac = "Діва"
    elif (M == 9 and D >= 23) or (M == 10 and D <= 22):
        zodiac = "Терези"
    elif (M == 10 and D >= 23) or (M == 11 and D <= 22):
        zodiac = "Скорпіон"
    elif (M == 11 and D >= 23) or (M == 12 and D <= 21):
        zodiac = "Стрілець"
    else:
        zodiac = "Козеріг"
    print("Знак Зодіаку:", zodiac)

def task12():
    while True:
        unit_input = input("Введіть номер одиниці маси (1-кілограм, 2-мілліграм, 3-грам, 4-тонна, 5-центнер): ")
        if unit_input.isdigit():
            unit = int(unit_input)
            if unit in [1, 2, 3, 4, 5]:
                break
    while True:
        mass_input = input("Введіть масу тіла у цих одиницях: ")
        if mass_input.replace('.', '', 1).isdigit():
            mass = float(mass_input)
            break
    kg = 0
    if unit == 1:
        kg = mass
    elif unit == 2:
        kg = mass / 1_000_000
    elif unit == 3:
        kg = mass / 1000
    elif unit == 4:
        kg = mass * 1000
    elif unit == 5:
        kg = mass * 100
    print(f"Маса тіла в кілограмах: {kg:.6f} кг")

if __name__ == "__main__":
    task1()
    task2()
    task4()
    task5()
    task8()
    task9()
    task10()
    task11()
    task12()
