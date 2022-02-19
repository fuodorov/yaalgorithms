n = int(input())
st = sorted([int(x) for x in input().split()], reverse=True)

for i in range(len(st) - 2):
    if st[i] < st[i + 1] + st[i + 2]:
        print(st[i] + st[i + 1] + st[i + 2])
        break
    else:
        i += 1
