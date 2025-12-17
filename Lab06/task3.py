import os


def task3():
    curr_dir = os.path.dirname(__file__)
    dir_task3 = os.path.join(curr_dir, 'files_task3')
    
    if not os.path.exists(dir_task3):
        os.makedirs(dir_task3)
    
    file_path = os.path.join(dir_task3, 'learning_python.txt')
    
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding='utf-8') as f:
            examples = [
                "Python можна використати для веб-розробки",
                "Python можна використати для аналізу даних та машинного навчання",
                "Python можна використати для автоматизації рутинних завдань",
                "Python можна використати для створення ігор",
                "Python можна використати для наукових обчислень та моделювання",
                "Python можна використати для розробки мобільних додатків",
                "Python можна використати для роботи з базами даних"
            ]
            for line in examples:
                f.write(f"{line}\n")
        print(f"Створено файл {file_path}")
    
    python_opportunities = []
    prefix = "Python можна використати для"

    print("\nОригінальні рядки з файлу:")
    with open(file_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith(prefix):
                python_opportunities.append(line)
                print(f"  {line}")
            elif line:
                print(f"  Помилка введення: {line}")
    
    python_opportunities.sort(key=len, reverse=True)
    
    print("\nВідсортовані рядки:")
    for i, line in enumerate(python_opportunities, 1):
        print(f"  {i}. {line} (довжина: {len(line)})")


task3()

