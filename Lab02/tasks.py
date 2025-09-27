import random
import math

def task1():
    numbers = [random.randint(0, 100) for _ in range(10)]
    print("Вхідні числа:", numbers)
    first_half = [x for x in numbers if x <= 50]
    print("Числа <=50:", first_half)

def task2():
    total = float(input("Введіть суму покупки: "))
    discount = 0
    if total > 1000:
        discount = 0.05
    elif total > 500:
        discount = 0.03
    final_price = total * (1 - discount)
    print(f"Сума до оплати з урахуванням знижки: {final_price:.2f} грн")

def task4():
    A = int(input("Введіть число A: "))
    B = int(input("Введіть число B (B > A): "))
    total_sum = 0
    for i in range(A, B+1):
        total_sum += i
    print(f"Сума чисел від {A} до {B}:", total_sum)

def task5():
    A = int(input("Введіть число A: "))
    B = int(input("Введіть число B (B > A): "))
    sum_squares = 0
    for i in range(A, B+1):
        sum_squares += i**2
    print(f"Сума квадратів чисел від {A} до {B}:", sum_squares)

def task8():
    N = int(input("Введіть число N (>1): "))
    K = 0
    while 5**K <= N:
        K += 1
    print(f"Найменше K, для якого 5^K > N: {K}")

def task9():
    n = int(input("Введіть число n: "))
    i = 1
    while True:
        square = i**2
        if square > n:
            print(f"Перше число у послідовності квадратів, більше {n}: {square}")
            break
        i += 1

def task10():
    n = int(input("Введіть число n: "))
    i = 0
    seq = []
    while True:
        if i == 0:
            num = 1
        else:
            num = i**2 - (i-1)**2  # або використовуємо рекурсію для 1,2,5,10,...
            num = seq[-1] + i*2 - 1  # точна формула для послідовності 1,2,5,10,17,26,...
        seq.append(num)
        if num > n:
            print(f"Перше число послідовності, більше {n}: {num}")
            break
        i += 1

def task11():
    D = int(input("Введіть день: "))
    M = int(input("Введіть місяць: "))
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
    unit = int(input("Введіть номер одиниці маси (1-кілограм, 2-мілліграм, 3-грам, 4-тонна, 5-центнер): "))
    mass = float(input("Введіть масу тіла у цих одиницях: "))
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
