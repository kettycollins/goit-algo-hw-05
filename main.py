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
    text = read_file('Algorythms/homework/goit-algo-hw-05/task 3/article1.txt')
    real_pattern = "some_real_pattern"
    fake_pattern = "some_fake_pattern"

    results = []
    for pattern in (real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text, pattern)
        results.append((boyer_moore_search.__name__, pattern, time))
        time = benchmark(kmp_search, text, pattern)
        results.append((kmp_search.__name__, pattern, time))
        time = benchmark(rabin_karp_search, text, pattern)
        results.append((rabin_karp_search.__name__, pattern, time))
    title = f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))
    for result in results:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")
