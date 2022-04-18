"""
ПРИНЦИП РАБОТЫ
    1.  Распакуем строки.
        По условию.
    2.  Найдем наибольший общий префикс распакованных строк.
        Ключ к решению проблемы - найти общий префикс двух строк.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    O(n*m), где n - количество строк, m - длина самой большой строки.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    O(n*m), где n - количество строк, m - длина самой большой строки.

УСПЕШНАЯ ПОСЫЛКА
    67490301
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


def max_prefix(strings):
    if len(strings) == 0:
        return ''

    prefix = strings[0]
    for string in strings[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]

    return prefix


packed_strings = [input() for _ in range(int(input()))]
unpacked_strings = [unpack(string) for string in packed_strings]
print(max_prefix(unpacked_strings))
