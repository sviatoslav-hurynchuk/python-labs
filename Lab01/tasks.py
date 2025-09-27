print("Завдання 1. Введіть два інтових і два флоат числа:")
a = int(input())
b = int(input())
c = float(input())
d = float(input())

print("\nЗавдання 2.")

results = [a + b, a - b, a * b]

if b != 0:
    results.append(a / b)
else:
    results.append("Ділення на нуль!")

# піднесення до степеня
results.append(a ** b)

# цілочисельне ділення
if b != 0:
    results.append(a // b)
else:
    results.append("Ділення на нуль!")

# остача від ділення
if b != 0:
    results.append(a % b)
else:
    results.append("Ділення на нуль!")

print("Результати:", results)

print("\nЗавдання 3.")
print("Кількість елементів у списку:", len(results))
print("Парні елементи списку:", [x for x in results if isinstance(x, (int, float)) and x % 2 == 0])

print("\nЗавдання 4.")
if len(results) >= 5:
    results[1], results[4] = results[4], results[1]
print("Список після обміну:", results)

print("\nЗавдання 5.")
name = input("Введіть ваше прізвище та ім'я: ")

print("\nВиконавець лабораторної роботи:")
print(name)
print("Висновки:")
print("У цій лабораторній роботі я навчився виконувати основні операції над числами.")
print("Навчився працювати зі списками у Python.")
print("Навчився вводити та виводити інформацію за допомогою input та print.")
