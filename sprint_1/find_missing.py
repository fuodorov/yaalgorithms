"""
ПРИНЦИП РАБОТЫ
    Используем множество. Преобразуем второй список во множество.
    Используем указатель и перезапишем первый список, оставляя только уникальные значения.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    O(n + m), где n, m - количество элементов в первом и во втором списках соответственно.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    O(n), где n - количество элементов в первом списке соответственно.
"""


def find_missing(first, second):
    second_set = set(second)
    unique_elements = 0

    for item in first:
        if item not in second_set:
            first[unique_elements] = item
            unique_elements += 1

    return first[:unique_elements]
