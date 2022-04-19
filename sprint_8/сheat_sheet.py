"""
ПРИНЦИП РАБОТЫ
    1.  Создадим префиксное дерево.
        В терминальные узлы будем записывать дополнительную информацию - длину слова.
    2.  Создадим массив с булевыми промежуточные значения - можно ли создать строку с данным индексом или же нет.
        Для каждого индекса будем проходить по префиксному дереву.
        Когда мы встречаем терминальный узел и при этом,
        ответ положительный и для строки без текущего рассматриваемого слова,
        тогда записываем в массив True.
        В противном случае записывается False.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    Построение префиксного дерева - O(L), где L — суммарная длина всех слов во множестве.
    Прохождение по префиксному дереву - O(n^2), где n - количество символов в строке.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Префиксное дерево - O(L), где L — суммарная длина всех слов во множестве.
    Массив - O(n), где n - количество символов в строке.

УСПЕШНАЯ ПОСЫЛКА
    67555610
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = {} if next is None else next
        self.terminal = False


def create_tree(words):
    root = Node('')
    for word in words:
        node = root
        for index, char in enumerate(word):
            node.next[char] = node.next.get(char, Node(char))
            node = node.next[char]
        node.terminal = len(word)
    return root


def is_split_words(string, words):
    root = create_tree(words)
    dp = [True] + [False] * len(string)
    for i in range(len(string)):
        node = root
        if dp[i]:
            for j in range(i, len(string) + 1):
                if node.terminal:
                    dp[j] = True
                if j == len(string) or not node.next.get(string[j], False):
                    break
                node = node.next[string[j]]
    return dp[-1]


string = input()
words = [input() for _ in range(int(input()))]
print('YES' if is_split_words(string, words) else 'NO')
