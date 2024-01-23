def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)

    if m == 0:
        return 0  # Паттерн порожній, повертаємо 0

    last_occurrence = {}  # Таблиця для останніх входжень символів паттерна
    for i in range(m - 1):
        last_occurrence[pattern[i]] = i

    i = m - 1
    j = m - 1

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i  # Знайдено входження
            else:
                i -= 1
                j -= 1
        else:
            # Зміщення вправо, використовуючи таблицю останніх входжень
            if text[i] in last_occurrence:
                i += m - min(j, 1 + last_occurrence[text[i]])
            else:
                i += m
            j = m - 1

    return -1  # Відповідне входження не знайдено
