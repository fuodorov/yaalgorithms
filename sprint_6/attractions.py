n, m = map(int, input().split())
graph = [[float("inf")] * n for _ in range(n)]

for it in range(m):
    r, c, w = map(int, input().split())
    if graph[r - 1][c - 1] == float("inf"):
        graph[r - 1][c - 1] = graph[c - 1][r - 1] = w

for it in range(n):
    graph[it][it] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph:
    for item in row:
        print(item if item != float("inf") else -1, end=' ')
    print()
