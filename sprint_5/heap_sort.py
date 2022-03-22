"""
ПРИНЦИП РАБОТЫ

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    Статья - https://habr.com/ru/company/edison/blog/495420/.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    Вики - https://ru.wikipedia.org/wiki/Пирамидальная_сортировка.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ

"""
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    __slots__ = ['username', 'solved', 'errors']
    username: str
    solved: int
    errors: int

    def key(self):
        return -self.solved, self.errors, self.username

    def __gt__(self, other):
        return self.key() > other.key()

    def __lt__(self, other):
        return other > self

    def __str__(self):
        return self.username


def heapsort(data):
    for start in range((len(data)-2)//2, -1, -1):
        heapsift(data, start, len(data) - 1)

    for end in range(len(data)-1, 0, -1):
        data[end], data[0] = data[0], data[end]
        heapsift(data, 0, end - 1)


def heapsift(data, start, end):
    root = start

    while True:
        child = root * 2 + 1

        if child > end:
            break

        if child + 1 <= end and data[child] < data[child+1]:
            child += 1

        if data[root] < data[child]:
            data[root], data[child], root = data[child], data[root], child
        else:
            break


n = int(input())
users = []

for _ in range(n):
    username, solved, errors = input().split()
    users.append(User(username, int(solved), int(errors)))

heapsort(users)

for person in users:
    print(person)
