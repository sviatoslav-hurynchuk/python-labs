import re


def task1_count_words_starting_with():
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


def main():
    while True:
        print("\nВиберіть завдання:")
        print("  1 - Пошук слів за початком")
        print("  0 - Вихід")

        choice = input("\nВаш вибір: ").strip()

        if choice == '1':
            task1_count_words_starting_with()
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
