"""
ПРИНЦИП РАБОТЫ

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ

ВРЕМЕННАЯ СЛОЖНОСТЬ

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ

"""


class HashTable:
    def __init__(self, size=10**5):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    @staticmethod
    def hashfunction(key, size):
        return key % size

    @staticmethod
    def rehash(oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def delete(self, key):
        data = self.get(key)
        self.put(key, None)
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __delitem__(self, key):
        return self.delete(key)


n = int(input())

hashtable = HashTable(n)


for _ in range(n):
    cmd = input().split()
    if len(cmd) == 2:
        print(getattr(hashtable, cmd[0])(int(cmd[1])))
    else:
        getattr(hashtable, cmd[0])(int(cmd[1]), int(cmd[2]))
