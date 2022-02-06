"""
ПРИНЦИП РАБОТЫ
    - Найти опорную точку
    - Разделить массив на два отсортированных массива
    - Выполнить бинарный поиск

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    Бинарный поиск – это алгоритм поиска, используемый для поиска целевых элементов в контейнере,
    где элементы должны быть расположены в порядке возрастания.
    Обычно двоичный поиск используется для поиска порядкового номера целевого элемента в отсортированном массиве.

    В бинарном поиске используется подход «разделяй и властвуй»,
    при котором массив делится на равные части до тех пор, пока не будет найден целевой элемент.

    Книга - Грокаем Алгоритмы А. Бхаргава.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    Бинарный поиск и поиск опорной точки имеют временную сложность O(log n).

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Бинарный поиск и поиск опорной точки имеют пространственную сложность O(1).

"""


def binary_search(arr, target, *, low=None, high=None):
    low = low if low else 0
    high = high if high else len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_pivot(arr, *, low=None, high=None):
    low = low if low else 0
    high = high if high else len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= arr[high]:
            low = mid + 1
        else:
            high = mid
    return high if high else len(arr) - 1


def broken_search(nums, target):
    pivot = find_pivot(nums)

    if nums[pivot] == target:
        return pivot

    return binary_search(nums, target, high=pivot-1) if nums[0] <= target else binary_search(nums, target, low=pivot+1)


def test():
    arr = [12, 41, 122, 411, 412, 1222, 3000, 12222, 122222]
    assert broken_search(arr, 3000) == 6
