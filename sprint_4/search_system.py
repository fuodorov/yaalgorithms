"""
ПРИНЦИП РАБОТЫ

    Серия статей на хабре - https://habr.com/ru/post/263823/, https://habr.com/ru/post/263913/

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ

ВРЕМЕННАЯ СЛОЖНОСТЬ

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ

"""
from collections import Counter
from itertools import chain


# input = [word1, word2, ...]
# output = {word1: [pos1, pos2], word2: [pos2, pos3], ...}
def index_one_file(term_list):
    file_index = {}
    for index, word in enumerate(term_list):
        if word in file_index.keys():
            file_index[word].append(index)
        else:
            file_index[word] = [index]
    return file_index


# input = {filename: [word1, word2, ...], ...}
# output = {filename: {word: [pos1, pos2, ...]}, ...}
def make_indices(term_lists):
    total = {}
    for filename in term_lists.keys():
        total[filename] = index_one_file(term_lists[filename])
    return total


# input = {filename: {word: [pos1, pos2, ...], ... }}
# output = {word: {filename: [pos1, pos2]}, ...}, ...}
def full_index(regdex):
    total_index = {}
    for filename in regdex.keys():
        for word in regdex[filename].keys():
            if word in total_index.keys():
                if filename in total_index[word].keys():
                    total_index[word][filename].extend(regdex[filename][word][:])
                else:
                    total_index[word][filename] = regdex[filename][word]
            else:
                total_index[word] = {filename: regdex[filename][word]}
    return total_index


def one_word_query(index, word):
    if word in index.keys():
        return chain(*[[filename] * len(index[word][filename]) for filename in index[word].keys()])
    else:
        return []


def free_text_query(index, string):
    result = []
    for word in set(string.split()):
        result += one_word_query(index, word)
    return [item[0] for item in Counter(sorted(result)).most_common()]


n = int(input())

documents = {}

for document in range(n):
    documents[document + 1] = input().split()

m = int(input())

for request in range(m):
    print(*free_text_query(full_index(make_indices(documents)), input())[:5])
