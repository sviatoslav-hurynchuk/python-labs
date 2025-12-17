import os


def task4():
    curr_dir = os.path.dirname(__file__)
    dir_task3 = os.path.join(curr_dir, 'files_task3')
    dir_task4 = os.path.join(curr_dir, 'files_task4')
    
    file_path = os.path.join(dir_task3, 'learning_python.txt')
    
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не знайдено!")
        print("Спочатку виконайте task3.py")
        return
    
    if not os.path.exists(dir_task4):
        os.makedirs(dir_task4)
        print(f"Створено каталог {dir_task4}")
    
    true_path = os.path.join(dir_task4, 'true_statements.txt')
    false_path = os.path.join(dir_task4, 'false_statements.txt')
    
    language = input("Введіть мову програмування замість Python: ").strip()
    
    with open(true_path, "w", encoding='utf-8') as f:
        f.write('')
    with open(false_path, "w", encoding='utf-8') as f:
        f.write('')
    
    true_statements = []
    false_statements = []
    
    with open(file_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            if line.startswith("Python можна використати для"):
                modified_line = line.replace("Python", language)
                
                print(f"\n{'-'*60}")
                print(f"Оригінал: {line}")
                print(f"Змінено:  {modified_line}")

                while True:
                    answer = input(f"Це актуально для {language}?: ").strip().lower()
                    if answer in ['так', 'ні', 'yes', 'no', 'y', 'n']:
                        break
                    print("Введіть 'так' або 'ні'")
                
                if answer in ['так', 'yes', 'y']:
                    true_statements.append(modified_line)
                    print("Додано до істинних тверджень")
                else:
                    false_statements.append(modified_line)
                    print("Додано до хибних тверджень")
    
    with open(true_path, "w", encoding='utf-8') as f:
        for line in true_statements:
            f.write(f"{line}\n")
    
    with open(false_path, "w", encoding='utf-8') as f:
        for line in false_statements:
            f.write(f"{line}\n")
    
    print("\n" + "="*60)
    print("ІСТИННІ ТВЕРДЖЕННЯ:")
    if true_statements:
        for i, stmt in enumerate(true_statements, 1):
            print(f"{i}. {stmt}")
    else:
        print("(немає)")
    
    print("ХИБНІ ТВЕРДЖЕННЯ:")
    if false_statements:
        for i, stmt in enumerate(false_statements, 1):
            print(f"{i}. {stmt}")
    else:
        print("(немає)")
    
    print(f"\nРезультати збережено:")
    print(f"  Істинні: {true_path}")
    print(f"  Хибні:   {false_path}")


task4()

