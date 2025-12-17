import os
import re
import csv
from datetime import datetime, date

class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):
        regex_pattern = re.compile(r"^[A-Za-zА-Яа-яЇїІіЄєҐґ'-]+(?: [A-Za-zА-Яа-яЇїІіЄєҐґ'-]+)*$")

        if not isinstance(surname, str) or not surname.strip() or not regex_pattern.fullmatch(surname):
            raise ValueError("Поле 'surname' невалідне")
        self.surname = surname.strip()

        if not isinstance(first_name, str) or not first_name.strip() or not regex_pattern.fullmatch(first_name):
            raise ValueError("Поле 'first_name' невалідне")
        self.first_name = first_name.strip()

        if nickname is not None:
            if not isinstance(nickname, str) or not nickname.strip() or not re.fullmatch(r"^[A-Za-z0-9_-]+$", nickname):
                raise ValueError("Поле 'nickname' невалідне")
            self.nickname = nickname.strip()
        else:
            self.nickname = None

        if isinstance(birth_date, str):
            if not birth_date.strip():
                raise ValueError("Поле 'birth_date' невалідне: порожній рядок")
            try:
                year, month, day = map(int, birth_date.split('-'))
                birth_date_obj = date(year, month, day)  # <- тут виправлено
            except ValueError:
                raise ValueError("Поле 'birth_date' невалідне")
        elif isinstance(birth_date, datetime):
            birth_date_obj = birth_date.date()
        elif isinstance(birth_date, date):
            birth_date_obj = birth_date
        else:
            raise ValueError("Поле 'birth_date' невалідне")

        if birth_date_obj > date.today():
            raise ValueError("Поле 'birth_date' невалідне: дата не може бути в майбутньому")

        self.birth_date = birth_date_obj

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1

        return str(age)

    def get_fullname(self):
        return "%s %s" % (self.surname, self.first_name)


def modifier(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл '{filename}' не знайдено")
    
    rows = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        
        if fieldnames is None:
            raise ValueError("Файл не містить заголовків колонок")
        
        rows = list(reader)
    
    if not rows:
        return
    
    persons = []
    for row in rows:
        surname = row.get('surname', row.get('Surname', ''))
        first_name = row.get('first_name', row.get('firstname', row.get('name', row.get('Name', ''))))
        birth_date = row.get('birth_date', row.get('birthdate', row.get('birth', '')))
        nickname = row.get('nickname', row.get('Nickname', None))
        
        if not surname or not first_name or not birth_date:
            print(f"Помилка: відсутні обов'язкові поля для рядка {row}")
            persons.append(None)
            continue
        
        try:
            person = Person(surname, first_name, birth_date, nickname if nickname else None)
            persons.append(person)
        except ValueError as e:
            print(f"Помилка створення об'єкта Person: {e}")
            persons.append(None)
            continue
    
    new_fieldnames = []
    name_index = None
    
    for i, field in enumerate(fieldnames):
        if field.lower() in ['name', 'first_name', 'firstname']:
            name_index = i
            break
    
    for i, field in enumerate(fieldnames):
        new_fieldnames.append(field)
        if i == name_index:
            new_fieldnames.append('fullname')
    
    new_fieldnames.append('age')
    
    new_rows = []
    for i, row in enumerate(rows):
        person = persons[i] if i < len(persons) else None
        new_row = dict(row)
        
        if person is not None:
            if name_index is not None:
                ordered_row = {}
                for j, field in enumerate(fieldnames):
                    ordered_row[field] = new_row[field]
                    if j == name_index:
                        ordered_row['fullname'] = person.get_fullname()
                ordered_row['age'] = person.get_age()
                new_rows.append(ordered_row)
            else:
                new_row['fullname'] = person.get_fullname()
                new_row['age'] = person.get_age()
                new_rows.append(new_row)
        else:
            if name_index is not None:
                ordered_row = {}
                for j, field in enumerate(fieldnames):
                    ordered_row[field] = new_row[field]
                    if j == name_index:
                        ordered_row['fullname'] = ''
                ordered_row['age'] = ''
                new_rows.append(ordered_row)
            else:
                new_row['fullname'] = ''
                new_row['age'] = ''
                new_rows.append(new_row)
    
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)


def task01():
    person = Person("Гуринчук", "Святослав", "2007-07-22", "lava")

    if person:
        print(person.get_fullname())
        print(person.get_age())

def current_work_path():
    return os.getcwd()

def file_path():
    return os.path.join(current_work_path(), "data.csv")

def task02():
    modifier(file_path())

task02()