import re


def task1():
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 1: Пошук слів за початком")
    print("=" * 60)

    text = input("Введіть текст (до 1000 слів): ").strip()
    if not text:
        print("Текст не може бути порожнім!")
        return

    words = re.findall(r'\w+', text, flags=re.UNICODE)
    word_count = len(words)

    print(f"Знайдено слів у тексті: {word_count}")

    if word_count > 1000:
        print(f"Забагато слів! Максимум 1000, а введено {word_count}.")
        return

    start_word = input("Введіть слово, з якого мають починатися інші слова: ").strip()
    if not start_word:
        print("Ви не ввели слово для пошуку!")
        return

    pattern = re.compile(r'\b' + re.escape(start_word), flags=re.IGNORECASE | re.UNICODE)

    count = sum(1 for w in words if pattern.match(w))

    matching_words = [w for w in words if pattern.match(w)]

    print("-" * 60)
    print(f"Кількість слів, що починаються з '{start_word}': {count}")
    if matching_words:
        print(f"Знайдені слова: {', '.join(matching_words[:10])}")
        if len(matching_words) > 10:
            print(f"   ... та ще {len(matching_words) - 10} слів")
    print("=" * 60)

def task2():
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 2: Замінити 'а' на 'А' у тексті")
    print("=" * 60)

    text = input("Введіть текст: ")
    if not text:
        print("Текст не може бути порожнім!")
        return

    new_text = text.replace('а', 'А')

    replaced_count = text.count('а')

    symbols_count = len(text)

    letters_count = sum(1 for ch in text if ch.isalpha())

    print("-" * 60)
    print(f"Новий текст: {new_text}")
    print(f"Кількість замін 'а' на 'А': {replaced_count}")
    print(f"Кількість символів у рядку: {symbols_count}")
    print(f"Кількість літер у рядку: {letters_count}")
    print("=" * 60)


def task3():
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 3: Підрахунок кількості входжень слова")
    print("=" * 60)

    text = input("Введіть текст: ").strip()
    if not text:
        print("Текст не може бути порожнім!")
        return

    word_to_find = input("Введіть слово для пошуку: ").strip()
    if not word_to_find:
        print("Слово для пошуку не може бути порожнім!")
        return

    pattern = re.compile(r'\b' + re.escape(word_to_find) + r'\b', flags=re.IGNORECASE | re.UNICODE)

    matches = pattern.findall(text)
    count = len(matches)

    print("-" * 60)
    print(f"Слово '{word_to_find}' зустрічається {count} раз(и) у тексті.")
    print("=" * 60)

def task4():
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 4: Перетворення тексту за умовами")
    print("=" * 60)

    text = input("Введіть текст (до 1000 слів): ").strip()
    if not text:
        print("Текст не може бути порожнім!")
        return

    words = re.findall(r"\w+(?:[’']\w+)*|[^\w\s’']", text, flags=re.UNICODE)
    word_only = [w for w in words if re.match(r"\w+(?:[’']\w+)*", w, flags=re.UNICODE)]

    if len(word_only) > 1000:
        print(f"Забагато слів! Максимум 1000, а введено {len(word_only)}.")
        return

    length = len(words)
    midpoint = length // 2

    result_first_half = []
    for w in words[:midpoint]:
        if re.match(r"\w+(?:[’']\w+)*", w, flags=re.UNICODE):
            w = w.capitalize()
        result_first_half.append(w)

    result_first_half.append('|')

    result_second_half = []
    for w in words[midpoint:]:
        if re.match(r"\w+(?:[’']\w+)*", w, flags=re.UNICODE):
            w = w.lower()
            result_second_half.append(w + '*')
        else:
            result_second_half.append(w)

    result = result_first_half + result_second_half
    output_text = ''.join(
        [(' ' + t if re.match(r"\w+(?:[’']\w+)*", t, flags=re.UNICODE) or t == '|' else t) for t in result]
    ).strip()

    print("-" * 60)
    print("Перетворений текст:")
    print(output_text)
    print("=" * 60)



def task5():
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 5: Слова що починаються на N та закінчуються на P")
    print("=" * 60)

    text = input("Введіть англійський текст (до 1000 слів): ").strip()
    if not text:
        print("Текст не може бути порожнім!")
        return

    words = re.findall(r'\w+|[^\w\s]', text)
    word_only = [w for w in words if w.isalpha()]

    if len(word_only) > 1000:
        print(f"Забагато слів! Максимум 1000, а введено {len(word_only)}.")
        return

    letter_start = input("Введіть літеру для початку слова (N): ").strip()
    letter_end = input("Введіть літеру для кінця слова (P): ").strip()

    if not (letter_start.isalpha() and letter_end.isalpha() and len(letter_start) == 1 and len(letter_end) == 1 and letter_start.isascii() and letter_end.isascii()):
        print("Помилка: Введені літери повинні бути однією англійською літерою.")
        return

    letter_start = letter_start.lower()
    letter_end = letter_end.lower()

    start_words = [w for w in word_only if w.lower().startswith(letter_start)]
    end_words = [w for w in word_only if w.lower().endswith(letter_end)]

    print("-" * 60)
    print(f"Слова, що починаються на '{letter_start.upper()}':")
    print(", ".join(start_words) if start_words else "Немає таких слів.")

    print(f"\nСлова, що закінчуються на '{letter_end.upper()}':")
    print(", ".join(end_words) if end_words else "Немає таких слів.")
    print("=" * 60)

def task6():
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 6: Підрахунок голосних літер в англійському тексті")
    print("=" * 60)

    text = input("Введіть текст (до 100 слів): ").strip()
    if not text:
        print("Текст не може бути порожнім!")
        return

    words = re.findall(r'\w+', text)
    if len(words) > 100:
        print(f"Забагато слів! Максимум 100, а введено {len(words)}.")
        return

    vowels = set('aeiouAEIOU')
    vowel_count = sum(ch.lower() in vowels for ch in text)

    print("-" * 60)
    print(f"Кількість голосних літер у тексті: {vowel_count}")
    print("=" * 60)

def task7():
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 7: Пошук імен та власних назв у тексті")
    print("=" * 60)

    text = input("Введіть англомовний текст (до 1000 слів): ").strip()
    if not text:
        print("Текст не може бути порожнім!")
        return

    tokens = re.findall(r'\w+|[^\w\s]', text)

    words = [w for w in tokens if re.match(r'\w+', w)]

    if len(words) > 1000:
        print(f"Забагато слів! Максимум 1000, а введено {len(words)}.")
        return

    proper_names = [word for word in words if word[0].isupper()]

    if proper_names:
        print("-" * 60)
        print("Вжиті імена та власні назви:")
        print(", ".join(proper_names))
    else:
        print("Імен та власних назв не знайдено.")
    print("=" * 60)

def main():
    while True:
        print("\nВиберіть завдання:")
        print("  1 - Пошук слів за початком")
        print("  2 - Замінити 'а' на 'А', підрахувати кількість замін, символів та літер")
        print("  3 - Підрахунок кількості входжень слова")
        print("  4 - Перетворення тексту за умовами")
        print("  5 - Слова що починаються на N та закінчуються на P")
        print("  6 - Підрахунок голосних літер в англійському тексті")
        print("  7 - Пошук імен та власних назв у тексті")
        print("  0 - Вихід")

        choice = input("\nВаш вибір: ").strip()

        if choice == '1':
            task1()
        elif choice == '2':
                task2()
        elif choice == '3':
                task3()
        elif choice == '4':
                task4()
        elif choice == '5':
                task5()
        elif choice == '6':
                task6()
        elif choice == '7':
                task7()
        elif choice == '0':
            break
        else:
            print("Ви ввели якусь фігню. Спробуйте ще раз")


if __name__ == "__main__":
    main()
