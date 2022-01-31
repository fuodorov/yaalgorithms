n = int(input())
m = int(input())

matrix = []

for row in range(n):
    matrix.append([int(value) for value in input().split()])

for column in range(m):
    print(*[matrix[row][column] for row in range(n)])