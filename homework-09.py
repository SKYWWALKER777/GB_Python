import numpy as np


def count_unique_elements(arr):
    unique_elements = np.unique(arr)
    count = len(unique_elements)
    return count


def has_duplicate_rows(arr):
    unique_rows, counts = np.unique(arr, axis=0, return_counts=True)
    has_duplicates = np.any(counts > 1)
    return has_duplicates


def find_min_max_indices(arr):
    min_index = np.unravel_index(np.argmin(arr), arr.shape)
    max_index = np.unravel_index(np.argmax(arr), arr.shape)
    diagonal_elements = np.diagonal(arr)
    return min_index, max_index, diagonal_elements


def main():
    arr1 = np.array([1, 2, 3, 4, 1, 2, 3])
    count = count_unique_elements(arr1)
    print(f"Количество уникальных элементов: {count}")

    arr2 = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
    has_duplicates = has_duplicate_rows(arr2)
    if has_duplicates:
        print("В массиве есть одинаковые строки")
    else:
        print("В массиве нет одинаковых строк")

    arr3 = np.random.randint(0, 10, size=(5, 5))
    min_index, max_index, diagonal_elements = find_min_max_indices(arr3)
    print(f"Индекс минимального элемента: {min_index}")
    print(f"Индекс максимального элемента: {max_index}")
    print(f"Элементы главной диагонали: {diagonal_elements}")


if __name__ == "__main__":
    main()
