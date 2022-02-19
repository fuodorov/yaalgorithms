with open("input.txt") as f:
    n = int(f.readline())
    factor = sorted(list(map(int, f.readline().split())), reverse=True)
    m = int(f.readline())
    sizes = sorted(list(map(int, f.readline().split())))

happy_child = 0

for i in range(len(factor)):
    if sizes and factor[i] <= sizes[-1]:
        sizes.pop()
        happy_child += 1

print(happy_child)
