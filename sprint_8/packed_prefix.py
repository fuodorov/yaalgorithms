"""
ПРИНЦИП РАБОТЫ
    1.  Распакуем строки.
        По условию.
    2.  Найдем наибольший общий префикс распакованных строк.
        Ключ к решению проблемы - найти общий префикс двух строк.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    O(n*m), где n - количество строк, m - длина самой большой строки.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    O(m), где m - длина самой большой строки.

УСПЕШНАЯ ПОСЫЛКА
    67533072
"""


def unpack(string):
    multiply, symbol, result = [], [], []
    for char in string:
        if char.isnumeric():
            multiply.append(int(char))
            continue
        if char == '[':
            symbol.append([])
            continue
        if char == ']':
            if len(symbol) == 1:
                result.append(''.join(symbol.pop()) * multiply.pop())
                continue
            previous = ''.join(symbol.pop())
            symbol[-1].append(previous * multiply.pop())
            continue
        if len(symbol) == 0:
            result.append(char)
            continue
        symbol[-1].append(char)

    return ''.join(result)


def max_prefix():
    n = int(input())

    if n == 0:
        return ''

    prefix = unpack(input())
    for _ in range(n-1):
        string = unpack(input())
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]

    return prefix


print(max_prefix())
