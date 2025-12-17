import os
import time
import re
from datetime import datetime


def task6():
    curr_dir = os.path.dirname(__file__)
    dir_task6 = os.path.join(curr_dir, 'files_task6')
    
    if not os.path.exists(dir_task6):
        os.makedirs(dir_task6)
    
    file_path = os.path.join(dir_task6, 'python_article.txt')
    result_path = os.path.join(dir_task6, 'analysis_result.txt')
    
    if not os.path.exists(file_path):
        sample_text = """Python is a high-level, interpreted programming language known for its simplicity and readability. Created by Guido van Rossum and first released in 1991, Python has become one of the most popular programming languages in the world.

Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented, and functional programming. Python is often described as a batteries included language due to its comprehensive standard library.

Python interpreters are available for many operating systems. A global community of programmers develops and maintains CPython, a free and open-source reference implementation. A non-profit organization, the Python Software Foundation, manages and directs resources for Python and CPython development.

Python is used in many application domains. Web development frameworks like Django and Flask are built with Python. In data science and machine learning, libraries such as NumPy, Pandas, and TensorFlow make Python the go-to language. Python is also popular in automation, scripting, and scientific computing.

The language's syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java. Python has a large and comprehensive standard library, which is often cited as one of its greatest strengths.

Python's development is conducted largely through the Python Enhancement Proposal process. The PEP process is the primary mechanism for proposing major new features, collecting community input on issues, and documenting Python design decisions.

Python 2.0 was released in 2000 and introduced many new features. Python 3.0, released in 2008, was a major revision that was not completely backward-compatible. Python 2 was discontinued in 2020, and all development efforts now focus on Python 3.

The Python community is known for being welcoming and supportive. There are numerous conferences, meetups, and online communities where Python enthusiasts can connect and learn from each other.

Python's versatility makes it suitable for beginners and experts alike. Its clear syntax makes it easy for newcomers to learn programming concepts, while its powerful features and extensive ecosystem make it valuable for experienced developers working on complex projects."""
        
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(sample_text)
        print(f"Створено файл з прикладом тексту: {file_path}\n")
    
    start_time = time.time()
    start_datetime = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    
    with open(file_path, "r", encoding='utf-8') as f:
        text = f.read()
    
    for char in text:
        if char.isalpha() and not ('a' <= char.lower() <= 'z'):
            print("Помилка: Завдання вимагає текст англійською мовою.")
            return
    
    word_count = len(text.split())
    print(f"Завантажено текст. Кількість слів: {word_count}")
    
    if word_count > 3000:
        print("Помилка: Текст містить більше 3000 слів")
        return
    
    letter_count = sum(1 for char in text if char.isalpha())
    if letter_count == 0:
        print("Текст не містить букв!")
        return
    
    text_lower = text.lower()
    
    print("\n" + "="*70)
    print("РЕЖИМИ АНАЛІЗУ:")
    print("-"*70)
    print("1 - Частота літер")
    print("2 - Частота слів (всі слова)")
    print("="*70)
    
    choice = None
    while choice not in ["1", "2"]:
        choice = input("Введіть номер режиму: ").strip()
        if choice not in ["1", "2"]:
            print("Невірний вибір. Спробуйте ще раз.\n")
    
    title = ""
    result_data = []
    
    if choice == "1":
        letter_freq = {}
        for char in text_lower:
            if char.isalpha():
                letter_freq[char] = letter_freq.get(char, 0) + 1
        
        sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
        title = "Частота літер у тексті"
        result_data = sorted_freq
        
    elif choice == "2":
        words = text_lower.split()
        word_freq = {}
        for word in words:
            word = re.sub(r'[^a-z]', '', word)
            if len(word) >= 2:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        title = "Частота всіх англійських слів у тексті (мінімум 2 символи)"
        result_data = sorted_freq
    
    end_time = time.time()
    execution_time = round(end_time - start_time, 4)
    last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%d.%m.%Y %H:%M:%S')
    
    print("\n" + "="*70)
    print(f"{title.upper()}")
    print("="*70)
    
    if result_data:
        for item, count in result_data:
            if choice == "1":
                print(f"  '{item}' - {count} разів")
            else:
                print(f"  {item} - {count} разів")
    else:
        print("  (немає даних)")
    
    print("="*70)
    print(f"Час виконання аналізу: {execution_time} сек")
    print("="*70)
    
    with open(result_path, "w", encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write(f"{'АНАЛІЗ ТЕКСТУ':^70}\n")
        f.write("="*70 + "\n\n")
        f.write(f"Час створення результату: {start_datetime}\n")
        f.write(f"Час останніх змін вихідного файлу: {last_modified}\n")
        f.write(f"Час виконання аналізу: {execution_time} сек\n")
        f.write(f"Кількість слів у тексті: {word_count}\n\n")
        f.write("="*70 + "\n")
        f.write(f"{title}\n")
        f.write("="*70 + "\n\n")
        
        if result_data:
            for item, count in result_data:
                if choice == "1":
                    f.write(f"'{item}' - {count} разів\n")
                else:
                    f.write(f"{item} - {count} разів\n")
        else:
            f.write("(немає даних)\n")
        
        f.write("\n" + "="*70 + "\n")
        f.write(f"Всього унікальних елементів: {len(result_data)}\n")
        f.write("="*70 + "\n")
    
    print(f"\nРезультати збережено у файл: {result_path}")


task6()

