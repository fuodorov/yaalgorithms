class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = {} if next is None else next
        self.terminale = False


def create_tree(words):
    root = Node('')
    for word in words:
        node = root
        for index, symbol in enumerate(word):
            new_node = Node(symbol)
            node.next[symbol] = node.next.get(symbol, new_node)
            if index == len(word) - 1:
                node.next[symbol].terminale = len(word)
            node = node.next[symbol]
    return root


def is_split_words(string, words):
    root = create_tree(words)
    len_string = len(string)
    dp = [False for _ in range(len_string + 1)]
    dp[0] = True
    node = root
    for i in range(len_string):
        offset = 0
        while i + offset < len_string + 1:
            if node.terminale and dp[i + offset - node.terminale]:
                dp[i + offset] = True
            if (i + offset == len(string) or not node.next.get(string[i + offset], False)):
                node = root
                break
            node = node.next[string[i + offset]]
            offset += 1
    return dp[-1]


if __name__ == '__main__':
    inp_string = input()
    count_words = int(input())
    inp_words = [input() for _ in range(count_words)]
    if is_split_words(inp_string, inp_words):
        print('YES')
    else:
        print('NO')