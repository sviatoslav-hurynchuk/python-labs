def analyze_nested_categories(data):
    totals = {}

    def process (item):
        if isinstance(item, dict):
            for key, value in item .items():
                totals[key] = totals.get(key, 0) + value

        elif isinstance(item, list):
            for sub in item:
                process (sub)

    process(data)
    categories = list(totals.keys())
    return categories, totals


nested_data = [
    [
        {"офіс": 100},
        {"маркетинг": 200}
    ],
    [
        [
            {"офіс": 50},
            {"маркетинг": 150}
        ],
        {"офіс": 200}
    ],
    {"офіс": 300},
    [{"офіс": 100, "extra": 1}]
]
result = analyze_nested_categories(nested_data)
print(result)