def filter_reports(reports, output_format, keyword):
    filtered_reports = []
    count = 0
    errors = []

    for report in reports:
        if not isinstance(report, tuple) or len(report) != 3:
            errors.append(report)
            continue

        title, pib, zvitFormat = report

        if not isinstance(title, str) or not isinstance(pib, str) or not isinstance(zvitFormat, str) \
                or not title or not pib or not zvitFormat:
            errors.append(report)
            continue

        if output_format == zvitFormat and (keyword in pib or keyword in title):
            filtered_reports.append(report)
            count += 1

    return {
        "filtered_reports": filtered_reports,
        "count": count,
        "errors": errors
    }


result = filter_reports(
    [
        ("Звіт1", "Іван Іванов", "pdf"),
        ("Звіт2", "Олена Петрівна", "docx"),
        ("", "Іван Іванов", "pdf"),  # некоректна назва
        ("Звіт3", "", "pdf"),  # некоректний автор
        ("Звіт4", "Петро Сидоров", ""),  # некоректний формат
        "не кортеж",  # невірний формат даних
        123,  # невірний формат даних
        None,  # невірний формат даних
        ("Звіт5",),  # невірний формат всередині кортежу
        ("Звіт6", "Іван Іванов"),  # невірний формат всередині кортежу
        ("Звіт7", "Іван Іванов", 123),  # невірний тип для формату
    ],
    "pdf",
    "Іва"
)
print(result)