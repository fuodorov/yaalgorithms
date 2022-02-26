"""
ПРИНЦИП РАБОТЫ

    Серия статей на хабре - https://habr.com/ru/post/263823/, https://habr.com/ru/post/263913/

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ

ВРЕМЕННАЯ СЛОЖНОСТЬ

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ

"""


# input = [word1, word2, ...]
# output = {word1: len1, word2: len2, ...}
def index_one_file(term_list):
    file_index = {}
    for word in term_list:
        if word in file_index.keys():
            file_index[word] += 1
        else:
            file_index[word] = 1
    return file_index


# {filename: [word1, word2, ...], ...} =>
# {filename: {word: len, ...}, ...} =>
# {word: {filename: len}, ...}, ...}
def full_index(files):
    index, indices = {}, {}
    for filename in files.keys():
        indices[filename] = index_one_file(files[filename])
        for word in indices[filename].keys():
            if word in index.keys():
                index[word][filename] = indices[filename][word]
            else:
                index[word] = {filename: indices[filename][word]}
    return index


def get_max(arr, limit):
    result = []
    for item in sorted(arr, reverse=True)[:limit]:
        if item > 0:
            index = arr.index(item)
            result.append(index)
            arr[index] = 0
    return result


def free_text_query(index, string, bd_size=10**4):
    result = [0] * bd_size
    for word in set(string.split()):
        if word in index.keys():
            for filename in index[word].keys():
                result[filename] += index[word][filename]
    return result


n = int(input())

documents = {document+1: input().split() for document in range(n)}
search_index = full_index(documents)

m = int(input())

for request in range(m):
    print(*get_max(free_text_query(search_index, input(), bd_size=n+1), limit=5))
