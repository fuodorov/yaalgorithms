"""
ПРИНЦИП РАБОТЫ
    Составляем остовное дерево. Храним самое тяжёлое ребро в куче, используя heapq.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    O(E*logV), где E - количество рёбер в графе, а V - количество вершин.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Хранение кучи - O(n).
    Список смежности - O(E*V), где E - количество вершин, V - количество рёбер.
"""
import heapq


def add_vertex(vertex, graph_edges, added, edges):
    added.add(vertex)

    for edge, weight in graph_edges:
        if edge not in added:
            heapq.heappush(edges, (-weight, edge))


n, m = map(int, input().split())
graph = {i+1: [] for i in range(n)}

for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append((t, w))
    graph[t].append((f, w))


added, edges = set(), []
maximum_spanning_tree = 0

add_vertex(1, graph[1], added, edges)

while len(added) != n and edges:
    weight, vertex = heapq.heappop(edges)
    if vertex not in added:
        maximum_spanning_tree += abs(weight)
        add_vertex(vertex, graph[vertex], added, edges)

print('Oops! I did it again' if len(added) != n else maximum_spanning_tree)
