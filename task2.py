def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    iterations = 0

    if upper_bound < x:
        return iterations, upper_bound

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return iterations, arr[mid]

    # якщо елемент не знайдений
    return iterations, upper_bound


if __name__ == '__main__':
    arr = [3.5, 4.2, 10.1, 40.7, 50.0, 60.3, 70.8, 80.5, 90.2, 100.9]
    x = 6.0

    iterations, upper_bound = binary_search(arr, x)

    if upper_bound == x:
        print(f"Element is present at index, number of iterations: {iterations}")
    else:
        print(f"Element is not present in array, upper bound: {upper_bound}")
