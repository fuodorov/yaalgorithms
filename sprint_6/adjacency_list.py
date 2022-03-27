from itertools import groupby

n, m = map(int, input().split())

edges = []

for it in range(m):
    r, c = map(int, input().split())
    edges.append((r, c))

adj = {k: [v[1] for v in g] for k, g in groupby(sorted(edges), lambda e: e[0])}

for row in range(1, n + 1):
    print(*[len(adj[row]), *adj[row]]) if adj.get(row) is not None else print(0)
