class Alphabet:
    __ua_lang = "Ua"
    __ua_letters = ['А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я']

    def __init__(self, lang=None, letters=None):
        if lang is None:
            lang = Alphabet.__ua_lang
        if letters is None:
            letters = Alphabet.__ua_letters

        if not isinstance(lang, str) or not lang.strip():
            raise ValueError("lang має бути непорожнім рядком")

        if isinstance(letters, str):
            letters_iter = list(letters)
        else:
            try:
                letters_iter = list(letters)
            except TypeError:
                raise TypeError("letters має бути рядком або ітерованою послідовністю символів")

        cleaned_letters = []
        for ch in letters_iter:
            if not isinstance(ch, str) or len(ch.strip()) != 1:
                raise ValueError("У алфавіті всі символи мають бути непорожніми рядками довжини 1")
            cleaned_letters.append(ch.strip())

        self.lang = lang.strip()
        self.letters = cleaned_letters

    def print_alphabet(self):
        for letter in self.letters:
            print(letter, end=' ')
        print()

    def letters_num(self):
        return len(self.letters)

    @staticmethod
    def is_ua_lang(text):
        if not isinstance(text, str):
            return False
        text_lower = text.lower()
        ua_letters_lower = ''.join([letter.lower() for letter in Alphabet.__ua_letters])
        for char in text_lower:
            if char.isalpha() and char in ua_letters_lower:
                return True
        return False


class EngAlphabet(Alphabet):
    __en_letters_num = 26

    def __init__(self):
        super().__init__("En", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    @staticmethod
    def is_en_letter(text):
        if not isinstance(text, str):
            return False
        if len(text) == 0:
            return False
        en_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        return all(char in en_letters for char in text)

    def letters_num(self):
        return EngAlphabet.__en_letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."


def task01():
    eng_alphabet = EngAlphabet()
    eng_alphabet.print_alphabet()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter("J"))
    alphabet = Alphabet()
    print(alphabet.is_ua_lang("Щ"))
    print(EngAlphabet.example())


task01()

