from datetime import datetime


def is_valid_date(date_str, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except (ValueError, TypeError):
        return False


def analyze_expenses(expenses):
    category_totals = {}
    max_expense = None
    invalid_dates = []
    errors = []

    for expense in expenses:
        if not isinstance(expense, tuple) or len(expense) != 3:
            errors.append(expense)
            continue

        amount, category, date = expense

        if not isinstance(amount, (int, float)) or amount is None:
            errors.append(expense)
            continue
        if not isinstance(category, str) or not category:
            errors.append(expense)
            continue
        if not isinstance(date, str) or not is_valid_date(date):
            if not is_valid_date(date):
                invalid_dates.append(date)
            errors.append(expense)
            continue

        category_totals[category] = category_totals.get(category, 0) + amount

        if max_expense is None or amount > max_expense[0]:
            max_expense = expense

    return {
        "category_totals": category_totals,
        "max_expense": max_expense,
        "invalid_dates": invalid_dates,
        "errors": errors
    }


result = analyze_expenses([
    (100, "офіс", "2024-06-01"),
    (200, "маркетинг", "2024-06-02"),
    (50, "офіс", "2024-13-01"),
    (None, "маркетинг", "2024-06-02"),  # некоректна сума
    (100, None, "2024-06-01"),  # некоректна категорія
    (100, "офіс", None),  # некоректна дата
    "не кортеж",  # невірний формат даних
    123,  # невірний формат даних
    None,  # невірний формат даних
    (100, "офіс"),  # невірний формат всередині кортежу
    (100,),  # невірний формат всередині кортежу
    (100, "офіс", "2024-06-01", "extra")  # зайвий елемент у кортежі
])
print(result)