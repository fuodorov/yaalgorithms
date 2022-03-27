from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(m):
    u, v = [int(i) - 1 for i in input().split()]
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * n
answer = 0
components = []

for i in range(n):
    if visited[i]:
        continue

    answer += 1
    visited[i] = True
    queue = [i]
    component = []
    while queue:
        v = queue.pop()
        component.append(v+1)
        for to in graph[v]:
            if not visited[to]:
                visited[to] = True
                queue.append(to)
    components.append(component)

print(answer)
for i in range(answer):
    print(*sorted(components[i]))
