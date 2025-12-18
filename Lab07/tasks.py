import os
import re
import csv
from datetime import datetime, date


class Person:
    NAME_PATTERN = re.compile(r"^[A-Za-zА-Яа-яЇїІіЄєҐґ'-]+(?: [A-Za-zА-Яа-яЇїІіЄєҐґ'-]+)*$")
    NICKNAME_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")

    def __init__(self, surname, first_name, birth_date, nickname=None):
        self._validate_field(surname, "surname", Person.NAME_PATTERN)
        self.surname = surname.strip()

        self._validate_field(first_name, "first_name", Person.NAME_PATTERN)
        self.first_name = first_name.strip()

        self.nickname = self._validate_optional_field(nickname, Person.NICKNAME_PATTERN)

        self.birth_date = self._parse_and_validate_date(birth_date)

    @staticmethod
    def _validate_field(value, field_name, pattern):
        if not isinstance(value, str) or not value.strip() or not pattern.fullmatch(value):
            raise ValueError(f"Поле '{field_name}' невалідне")

    @staticmethod
    def _validate_optional_field(value, pattern):
        if value is None:
            return None
        if not isinstance(value, str) or not value.strip() or not pattern.fullmatch(value):
            raise ValueError("Поле 'nickname' невалідне")
        return value.strip()

    def _parse_and_validate_date(self, birth_date):
        if isinstance(birth_date, str):
            if not birth_date.strip():
                raise ValueError("Поле 'birth_date' невалідне: порожній рядок")
            try:
                year, month, day = map(int, birth_date.split('-'))
                birth_date_obj = date(year, month, day)
            except ValueError:
                raise ValueError("Поле 'birth_date' невалідне")
        elif isinstance(birth_date, (datetime, date)):
            birth_date_obj = birth_date.date() if isinstance(birth_date, datetime) else birth_date
        else:
            raise ValueError("Поле 'birth_date' невалідне")

        if birth_date_obj > date.today():
            raise ValueError("Поле 'birth_date' невалідне: дата не може бути в майбутньому")
        return birth_date_obj

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"


class CSVProcessor:
    FIELD_ALIASES = {
        'surname': ['surname', 'Surname'],
        'first_name': ['first_name', 'firstname', 'name', 'Name'],
        'birth_date': ['birth_date', 'birthdate', 'birth'],
        'nickname': ['nickname', 'Nickname']
    }

    NAME_FIELDS = {'name', 'first_name', 'firstname'}

    @staticmethod
    def read_csv(filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл '{filename}' не знайдено")

        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                raise ValueError("Файл не містить заголовків колонок")
            return list(reader), reader.fieldnames

    @staticmethod
    def extract_person_data(row):
        data = {}
        for field, aliases in CSVProcessor.FIELD_ALIASES.items():
            for alias in aliases:
                if alias in row and row[alias].strip():
                    data[field] = row[alias]
                    break

        valid = all(data.get(key) for key in ['surname', 'first_name', 'birth_date'])
        return {'valid': valid, 'data': data}

    @staticmethod
    def create_persons(rows):
        persons = []
        for row in rows:
            person_data = CSVProcessor.extract_person_data(row)
            if not person_data['valid']:
                print(f"Помилка: відсутні обов'язкові поля для рядка {row}")
                persons.append(None)
                continue
            try:
                person = Person(**person_data['data'])
                persons.append(person)
            except ValueError as e:
                print(f"Помилка створення об'єкта Person: {e}")
                persons.append(None)
        return persons

    @staticmethod
    def find_name_column(fieldnames):
        return next((i for i, field in enumerate(fieldnames)
                     if field.lower() in CSVProcessor.NAME_FIELDS), None)

    @staticmethod
    def build_new_fieldnames(fieldnames, name_index):
        new_fieldnames = fieldnames[:]
        if name_index is not None:
            new_fieldnames.insert(name_index + 1, 'fullname')
        else:
            new_fieldnames.append('fullname')
        new_fieldnames.append('age')
        return new_fieldnames

    @staticmethod
    def process_row(row, person, fieldnames, name_index):
        new_row = dict(row)

        if person:
            new_row['fullname'] = person.get_fullname()
            new_row['age'] = person.get_age()

            if name_index is not None:
                # Зберігаємо порядок полів
                ordered_row = {field: new_row[field] for field in fieldnames}
                ordered_row['fullname'] = new_row['fullname']
                ordered_row['age'] = new_row['age']
                return ordered_row
        else:
            new_row['fullname'] = ''
            new_row['age'] = ''

        return new_row

    @staticmethod
    def process_rows(rows, persons, fieldnames, name_index):
        return [CSVProcessor.process_row(row, persons[i] if i < len(persons) else None,
                                         fieldnames, name_index)
                for i, row in enumerate(rows)]

    @staticmethod
    def write_csv(filename, fieldnames, rows):
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def process_file(filename):
        rows, fieldnames = CSVProcessor.read_csv(filename)
        if not rows:
            return

        persons = CSVProcessor.create_persons(rows)
        name_index = CSVProcessor.find_name_column(fieldnames)
        new_fieldnames = CSVProcessor.build_new_fieldnames(fieldnames, name_index)
        new_rows = CSVProcessor.process_rows(rows, persons, fieldnames, name_index)
        CSVProcessor.write_csv(filename, new_fieldnames, new_rows)


def get_file_path():
    return os.path.join(os.getcwd(), "data.csv")


def task01():
    person = Person("Гуринчук", "Святослав", "2007-07-22", "lava")
    print(person.get_fullname())
    print(person.get_age())


def task02():
    CSVProcessor.process_file(get_file_path())


if __name__ == "__main__":
    task02()
