import functools


def mycmp(a, b):
    return -1 if (a[0] * 10 ** len(b[1]) + b[0]) > (b[0] * 10 ** len(a[1]) + a[0]) else 1


input()
array = [tuple([int(x), x]) for x in input().split(' ')]
array.sort(key=functools.cmp_to_key(mycmp))
print(''.join([x[1] for x in array]), end='')
