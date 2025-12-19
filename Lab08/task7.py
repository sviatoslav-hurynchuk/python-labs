class DecimalToRoman:
    ROMAN_NUMERALS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    @staticmethod
    def convert(decimal):
        if not isinstance(decimal, int) or decimal <= 0:
            raise ValueError("Число має бути додатнім цілим")
        if decimal > 3999:
            raise ValueError("Число не може бути більше 3999")

        result = []
        for value, numeral in DecimalToRoman.ROMAN_NUMERALS:
            count = decimal // value
            result.append(numeral * count)
            decimal %= value
        return "".join(result)


class RomanToDecimal:
    ROMAN_VALUES = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    @staticmethod
    def convert(roman):
        if not isinstance(roman, str):
            raise ValueError("Римське число має бути рядком")

        roman = roman.upper().strip()
        if not roman:
            raise ValueError("Римське число не може бути порожнім")

        result = 0
        prev_value = 0

        for char in reversed(roman):
            if char not in RomanToDecimal.ROMAN_VALUES:
                raise ValueError(f"Невідомий символ '{char}' в римському числі")

            value = RomanToDecimal.ROMAN_VALUES[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value

        return result


def task07():
    converter_to_roman = DecimalToRoman()
    numbers = [1, 4, 9, 27, 49, 100, 500, 1000, 1994, 2024]
    for num in numbers:
        roman = converter_to_roman.convert(num)
        print(f"{num} = {roman}")

    print()

    converter_to_decimal = RomanToDecimal()
    roman_numbers = ["I", "IV", "IX", "XXVII", "XLIX", "C", "D", "M", "MCMXCIV", "MMXXIV"]
    for roman in roman_numbers:
        decimal = converter_to_decimal.convert(roman)
        print(f"{roman} = {decimal}")


task07()

