"""
ПРИНЦИП РАБОТЫ
    Подробное описание алгоритма - https://ru.wikipedia.org/wiki/Расстояние_Левенштейна
    *Будем двигаться по рядам матрицы, используя только текущий ряд и предыдущий.

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    Доказательство алгоритма - https://ru.wikipedia.org/wiki/Расстояние_Левенштейна

ВРЕМЕННАЯ СЛОЖНОСТЬ
    O(n*m), где n и m — длины строк.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    O(n), где n - длина наименьшей строки.

УСПЕШНАЯ ПОСЫЛКА
    67425496
"""


def levenshtein_distance(first_str, second_str):
    n, m = len(first_str), len(second_str)
    if n > m:
        first_str, second_str, n, m = second_str, first_str, m, n

    current = list(range(n + 1))
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            current[j] = min(
                previous[j] + 1,
                current[j - 1] + 1,
                previous[j - 1] + 1 if first_str[j - 1] != second_str[i - 1] else previous[j - 1]
            )
    return current[n]


print(levenshtein_distance(input(), input()))
