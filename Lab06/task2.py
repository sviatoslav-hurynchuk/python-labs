import os


def task2():
    curr_dir = os.path.dirname(__file__)
    dir_task2 = os.path.join(curr_dir, 'files_task2')

    if not os.path.exists(dir_task2):
        os.makedirs(dir_task2)

    file_path = os.path.join(dir_task2, 'num.txt')

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding='utf-8') as f:
            f.write('')

    def add_numbers():
        numbers_input = input("Введіть цілі числа через пробіл: ").strip()
        numbers = numbers_input.split()
        valid_numbers = []

        for num in numbers:
            try:
                valid_numbers.append(int(num))
            except ValueError:
                print(f"Пропущено невалідне значення: {num}")
                continue

        with open(file_path, "w", encoding='utf-8') as f:
            for num in valid_numbers:
                f.write(f"{num}\n")

        print(f"Збережено {len(valid_numbers)} чисел у файл {file_path}")

    def check_parity():
        result_path = os.path.join(dir_task2, 'parity.txt')

        with open(file_path, "r", encoding='utf-8') as f:
            numbers = f.readlines()

        with open(result_path, "w", encoding='utf-8') as f:
            for line in numbers:
                try:
                    num = int(line.strip())
                    if num % 2 == 0:
                        f.write(f"{num} - парне\n")
                    else:
                        f.write(f"{num} - непарне\n")
                except ValueError:
                    continue

        print(f"\nРезультат аналізу парності збережено у файл {result_path}")

    add_numbers()
    check_parity()


task2()

