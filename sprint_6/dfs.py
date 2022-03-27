from itertools import groupby

n, m = map(int, input().split())

edges = []

for it in range(m):
    r, c = map(int, input().split())
    edges.append((r, c))
    edges.append((c, r))

adj = {k: [v[1] for v in g] for k, g in groupby(sorted(edges), lambda e: e[0])}

for row in range(1, n+1):
    if adj.get(row) is None:
        adj[row] = []


def dfs_iterative(graph, start_vertex):
    visited = set()
    traversal = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            stack.extend(reversed(graph[vertex]))
    return traversal


print(*dfs_iterative(adj, int(input())))