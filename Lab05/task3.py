import re


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def analyze_clients(clients):
    status_count = {}
    invalid_emails = []
    new_clients = []
    errors = []

    for client in clients:
        if not isinstance(client, tuple) or len(client) != 3:
            errors.append(client)
            continue

        name, status, email = client

        if not isinstance(name, str) or not isinstance(status, str) or not isinstance(email, str):
            errors.append(client)
            continue

        empty_name = not name.strip()
        empty_status = not status.strip()
        empty_email = not email.strip()

        invalid_email = not is_valid_email(email) if email.strip() else True

        if status.strip():
            status_count[status] = status_count.get(status, 0) + 1
            if status == "новий" and name.strip():
                new_clients.append(name)

        if empty_email or invalid_email:
            invalid_emails.append(email)

        if empty_name or empty_status or empty_email or invalid_email:
            errors.append(client)

    return {
        "status_count": status_count,
        "invalid_emails": invalid_emails,
        "new_clients": new_clients,
        "errors": errors
    }


result = analyze_clients([
    ("Іван", "новий", "ivan@email.com"),
    ("Олена", "постійний", "olena@mail.com"),
    ("", "новий", "ivan@email.com"),  # некоректне ім'я
    ("Олена", "", "olena[at]mail.com"),  # некоректний статус
    ("Іван", "", ""),  # некоректний email
    ("", "", ""),  # два некоректних поля (ім'я і статус)
    ("Петро", "", ""),  # два некоректних поля (статус і email)
    "не кортеж",  # невірний формат даних
    123,  # невірний формат даних
    None,  # невірний формат даних
    ("Олена",),  # невірний формат всередині кортежу
    ("Іван", "новий"),  # невірний формат всередині кортежу
    (123, "новий", "ivan@email.com"),  # невірний тип для імені
    ("Іван", 123, "ivan@email.com"),  # невірний тип для статусу
    ("Іван", "новий", 123),  # невірний тип для email
])
print(result)