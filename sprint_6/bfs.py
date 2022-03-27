import collections
from itertools import groupby

n, m = map(int, input().split())

edges = []

for it in range(m):
    r, c = map(int, input().split())
    edges.append((r, c))
    edges.append((c, r))

adj = {k: [v[1] for v in g] for k, g in groupby(sorted(edges), lambda e: e[0])}

for row in range(1, n + 1):
    if adj.get(row) is None:
        adj[row] = []


def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


bfs(adj, int(input()))
