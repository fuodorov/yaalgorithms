"""
ПРИНЦИП РАБОТЫ
    Есть два основный этапа в разработке поискового движка:
    построение индекса, а затем, используя индекс, ответить на запрос.

    Первый шаг в построении текстового поискового движка — это сборка перевёрнутого индекса.
    Перевёрнутый индекс — это структура данных, которая сопоставляет маркеры с документами,
    в который они появляются. В данном контексте мы можем рассматривать маркер просто как слова,
    таким образом перевёрнутый индекс, в своей основе, это что-то,
    что берёт слово и возвращает нам список документов, где оно встречается.

    На вход системе будут подаваться запросы.
    Запрос —– некоторый набор слов. По запросу надо вывести 5 самых релевантных документов.
    Релевантность документа оценивается следующим образом:
    для каждого уникального слова из запроса берётся число его вхождений в документ,
    полученные числа для всех слов из запроса суммируются.
    Итоговая сумма и является релевантностью документа.
    Чем больше сумма, тем больше документ подходит под запрос.
    Сортировка документов на выдаче производится по убыванию релевантности.
    Если релевантности документов совпадают —– то по возрастанию их порядковых номеров в базе.

    Серия статей на хабре - https://habr.com/ru/post/263823/, https://habr.com/ru/post/263913/.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    n - количество документов, m -количество запросов.
    Построение индекса - О(n^2).
    Запрос - О(m).

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Требуется О(n) памяти для построения поискового индекса.

"""
from collections import Counter, defaultdict


# {filename: [word1, word2, ...], ...} =>
# {filename: {word: len, ...}, ...} =>
# {word: {filename: len}, ...}, ...}
def full_index(files):
    index = defaultdict(dict)
    for filename, words in enumerate(files):
        files[filename] = dict(Counter(words))
        for word, weight in files[filename].items():
            index[word][filename] = weight
    return index


def get_max(arr, limit):
    result = []
    for item in sorted(arr, reverse=True)[:limit]:
        if item > 0:
            index = arr.index(item)
            result.append(index)
            arr[index] = 0
    return result


def free_text_query(index, string, n_docs=10**4):
    result = [0] * n_docs
    for word in set(string.split()):
        if word in index.keys():
            for filename, weight in index[word].items():
                result[filename] += weight
    return result


n = int(input())

documents = [[]] + [input().split() for document in range(n)]
search_index = full_index(documents)

m = int(input())

for request in range(m):
    print(*get_max(free_text_query(search_index, input(), n_docs=n+1), limit=5))
