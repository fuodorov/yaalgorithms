d = {}


def generator(n):
    def get_gen(k):
        if k not in d:
            d[k] = generator(k)
        return d[k]

    if n <= 0:
        return set([''])

    new_data = set()
    for i in get_gen(n - 1):
        new_data.add('(' + i + ')')
        new_data.add(i + '()')
        new_data.add('()' + i)

    for j in range(2, n // 2 + 1):
        b = get_gen(j)
        for i in get_gen(n - j):
            for k in b:
                new_data.add(i + k)
                new_data.add(k + i)

    return new_data


n = int(input())
print('\n'.join(sorted(generator(n))), end='')
