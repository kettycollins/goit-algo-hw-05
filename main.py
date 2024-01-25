import timeit
from bm import boyer_moore_search
from kmp import kmp_search
from rabina import rabin_karp_search

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def benchmark(func, text, pattern):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text, 'pattern': pattern}, number=10)

if __name__ == '__main__':
    text1 = read_file('Algorythms/homework/goit-algo-hw-05/task 3/article1.txt')
    text2 = read_file('Algorythms/homework/goit-algo-hw-05/task 3/article2.txt')
    
    real_pattern = "структури даних"
    fake_pattern = "мамуля"

    results1 = []
    for pattern in (real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text1, pattern)
        results1.append((boyer_moore_search.__name__, pattern, time))
        time = benchmark(kmp_search, text1, pattern)
        results1.append((kmp_search.__name__, pattern, time))
        time = benchmark(rabin_karp_search, text1, pattern)
        results1.append((rabin_karp_search.__name__, pattern, time))

    results2 = []
    for pattern in (real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text2, pattern)
        results2.append((boyer_moore_search.__name__, pattern, time))
        time = benchmark(kmp_search, text2, pattern)
        results2.append((kmp_search.__name__, pattern, time))
        time = benchmark(rabin_karp_search, text2, pattern)
        results2.append((rabin_karp_search.__name__, pattern, time))

    print("Результати для першої статті:")
    title = f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))
    for result in results1:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")

    print("\nРезультати для другої статті:")
    title = f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))
    for result in results2:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")
