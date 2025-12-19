import os
from datetime import datetime


def task5():
    curr_dir = os.path.dirname(__file__)
    dir_task5 = os.path.join(curr_dir, 'files_task5')
    
    if not os.path.exists(dir_task5):
        os.makedirs(dir_task5)
    
    file_path = os.path.join(dir_task5, 'guest_book.txt')
    
    file_exists = os.path.exists(file_path)
    creation_time = datetime.fromtimestamp(os.path.getctime(file_path)) if file_exists else datetime.now()

    if not file_exists:
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(f"{'ГОСТЬОВА КНИГА'}\n")
            f.write(f"Файл створено: {creation_time.strftime('%d.%m.%Y %H:%M:%S')}\n")
        print(f"Створено новий файл гостьової книги: {file_path}\n")
    else:
        print(f"Відкрито існуючий файл гостьової книги\n")
    
    def is_valid_name(nname):
        for char in nname:
            if not (char.isalpha() or char in ['-', "'"]):
                return False
        return True
    
    print("Вітаємо в гостьовій книзі!")
    print("Введіть '0' для завершення роботи\n")
    
    guests_count = 0
    
    while True:
        name = input("Введіть ваше ім'я: ").strip()
        
        if name.lower() in ['0']:
            break
        
        if not name:
            print("Ім'я не може бути порожнім. Спробуйте ще раз.\n")
            continue
        
        if not is_valid_name(name):
            print("Помилка в введенні імені. Використовуйте тільки літери.\n")
            continue
        
        current_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        greeting = f"Вітаємо, {name}!"
        
        print(f"\n✓ {greeting}\n")
        
        with open(file_path, "a", encoding='utf-8') as f:
            f.write(f"[{current_time}] {greeting}\n")
        
        guests_count += 1
    
    if guests_count > 0:
        last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%d.%m.%Y %H:%M:%S')
        
        with open(file_path, "a", encoding='utf-8') as f:
            f.write(f"\n{'='*70}\n")
            f.write(f"Файл створено: {creation_time.strftime('%d.%m.%Y %H:%M:%S')}\n")
            f.write(f"Останні внесені зміни: {last_modified}\n")
            f.write(f"Всього гостей у цій сесії: {guests_count}\n")
            f.write(f"{'='*70}\n")
        
        print(f"\n{'='*70}")
        print(f"Всього записано гостей: {guests_count}")
        print(f"Дані збережено у файл: {file_path}")
        print(f"{'='*70}")
    else:
        print("\nНе було додано жодного гостя.")


task5()

