def rabin_karp_search(text, pattern):
    d = 256  # Розмір алфавіту (ASCII)
    q = 101  # Просте число

    m = len(pattern)
    n = len(text)
    p = 0  # Хеш для паттерну
    t = 0  # Хеш для тексту
    h = 1

    # Обчислення h = pow(d, m-1)%q
    for i in range(m - 1):
        h = (h * d) % q

    # Обчислення початкового хеша для паттерну та першого вікна тексту
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        # Перевірка, чи хеш паттерну та поточного вікна тексту співпадає
        if p == t:
            # Перевірка символ за символом, чи співпадають
            match = True
            for j in range(m):
                if pattern[j] != text[i + j]:
                    match = False
                    break
            if match:
                return i  # Знайдено входження

        # Обчислення хешу для наступного вікна тексту
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q

    return -1  # Відповідне входження не знайдено
