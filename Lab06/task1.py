import os

def task1():
    sum_numbers = 0
    curr_dir = os.path.dirname(__file__)
    dir_task1 = os.path.join(curr_dir, 'files_task1')

    if not os.path.exists(dir_task1):
        os.makedirs(dir_task1)

    file_path = os.path.join(dir_task1, 'numbers.txt')

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding='utf-8') as f:
            for i in range(1, 11):
                f.write(f"{i * 5}\n")
        print(f"Створено файл {file_path} з 10 числами")

    with open(file_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            try:
                num = int(line)
                sum_numbers += num
            except ValueError:
                continue

    file_sum_path = os.path.join(dir_task1, 'sum_numbers.txt')
    with open(file_sum_path, "w", encoding='utf-8') as f:
        f.write(str(sum_numbers))

    print(f"Сума чисел: {sum_numbers}")
    print(f"Результат збережено у файл {file_sum_path}")


task1()