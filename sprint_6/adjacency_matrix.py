n, m = map(int, input().split())
adj = [[0] * n for _ in range(n)]

for it in range(m):
    r, c = map(int, input().split())
    adj[r - 1][c - 1] = 1

for row in adj:
    print(*row)