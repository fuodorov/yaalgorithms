"""
ПРИНЦИП РАБОТЫ
    Получим граф - если для одного из типов дороги поменять направление ребра.
    Для каждой вершины запускаем обход DFS, если граф имеет цикл, значит путь неоптимальный.

    Обнаружение цикла в ориентированном графе с использованием цветов -
    https://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/

    С помощью функции dfs_is_cyclic() определяем истинность утверждения оптимальности карты железных дорог.
    Для удобства определения уже посещенных городов (вершин) создаем отдельный "цветовой" массив, где будем
    помечать вершины тремя цветами:
    - белый - не посещенный город,
    - серый - уже посещенный, но не все его ребра обработаны,
    - черный - город уже посещен и все его ребра обработаны.

    Таким образом, если в процессе обхода графа мы наткнемся на серый город, это означает, что в графе есть цикл.
    Это означает, что существует пара городов, между которыми есть маршрут с разным типом дорог и
    карта железных дорог в этом случае является не оптимальной.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    O(V+E) - как в DFS со списками смежности.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    O(E*V) - список смежности, где E - количество вершин, V - количество рёбер.

УСПЕШНАЯ ПОСЫЛКА
    66717318
"""
import sys

WHITE = 0
GRAY = 1
BLACK = 2

WIDE_ROAD = 'B'
NARROW_ROAD = 'R'


class UnknownRoadTypeException(Exception):
    def __init__(self):
        pass


def dfs_is_cyclic(start_vertex, adjacency, colors):
    stack = [start_vertex]

    while stack:
        v = stack.pop()
        if colors[v] == WHITE:
            colors[v] = GRAY
            stack.append(v)

            for w in adjacency[v]:
                if colors[w] == WHITE:
                    stack.append(w)
                elif colors[w] == GRAY:
                    return True
        elif colors[v] == GRAY:
            colors[v] = BLACK

    return False


def is_cyclic(adjacency):
    colors = [WHITE] * len(adjacency)

    for i in range(len(adjacency)):
        if dfs_is_cyclic(i, adjacency, colors):
            return True

    return False


n = int(sys.stdin.readline().rstrip())
adjacency = {v: [] for v in range(0, n)}


for i in range(n-1):
    for j, type_road in enumerate(sys.stdin.readline().rstrip()):
        if type_road == WIDE_ROAD:
            adjacency[i].append(i+j+1)
        elif type_road == NARROW_ROAD:
            adjacency[i+j+1].append(i)
        else:
            raise UnknownRoadTypeException


print('NO' if is_cyclic(adjacency) else 'YES')
