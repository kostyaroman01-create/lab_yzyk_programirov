test_strings = ["Hello", "", "False", "0", "1", "   "]

for s in test_strings:
    bool_value = bool(s)
    print(f"Строка: '{s}' -> Логическое значение: {bool_value} (тип: {type(bool_value)})")