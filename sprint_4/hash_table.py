"""
ПРИНЦИП РАБОТЫ
    Абстрактный тип данных Map можно определить следующим образом.
    Его структура - неупорядоченная коллекция ассоциаций между ключами и значениями.
    Все ключи уникальны, таким образом поддерживаются отношения “один к одному” между ключами и значениями.

    Мы используем два списка, чтобы создать класс HashTable, воплощающий абстрактный тип данных Map.
    Один список, называемый slots, будет содержать ключи элементов,
    а параллельный ему список data - значения данных.
    Когда мы находим ключ, на соответствующей позиции в списке с данными будет находиться связанное с ним значение.

    hash функция реализует простой метод остатков.
    В качестве техники разрешения коллизий используется линейное пробирование с функцией повторного хэширования.

    Функция put предполагает, что в конце-концов найдётся пустой слот, или такой ключ уже присутствует в self.slots.
    Она вычисляет оригинальное хэш-значение и, если слот не пуст, применяет функцию rehash до тех пор,
    пока не найдёт свободное место. Если непустой слот уже содержит ключ, старое значение будет заменено на новое.

    Аналогично функция get начинает с вычисления начального хэш-значения.
    Если искомая величина не содержится в этом слоте, то используется rehash для определения следующей позиции.

    Вдохновлен - http://aliev.me/runestone/SortSearch/Hashing.html

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    Проблема коллизий. Когда два элемента хэшируются в один слот,
    нам требуется систематический метод для размещения в хэш-таблице второго элемента.
    Одним из методов разрешения коллизий является просмотр хэш-таблицы и
    поиск другого свободного слота для размещения в нём элемента, создавшего проблему.
    Простой способ сделать это - начать с оригинальной позиции хэш-значения и
    перемещаться по слотам определённым образом до тех пор, пока не будет найден пустой.
    Нам может понадобиться вернуться обратно к первому слоту (циклически), чтобы охватить хэш-таблицу целиком.
    Этот процесс разрешения коллизий называется открытой адресацией,
    поскольку пытается найти следующий свободный слот (или адрес) в хэш-таблице.
    Систематически посещая каждый слот по одному разу,
    мы действуем в соответствии с техникой открытой адресации, называемой линейным пробированием.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    Когда мы хотим найти элемент, мы просто используем хэш-функцию,
    чтобы вычислить имя слота элемента и затем проверить по таблице его наличие.
    Эта операция поиска имеет O(1), поскольку на вычисление хэш-значения требуется константное время,
    как и на переход по найденному индексу.
    Если всё находится там, где ему положено, то мы получаем алгоритм поиска за константное время.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Map, максимальный размер которого определяется заданным числом k, занимает O(k) памяти.

"""


class HashTable:
    def __init__(self, size=10**5):
        self._size = size
        self._slots = [None] * self._size
        self._data = [None] * self._size

    def put(self, key, data):
        slot = self.hash(key)

        if self._slots[slot] is None:
            self._slots[slot] = key
            self._data[slot] = data
        elif self._slots[slot] == key:
            self._data[slot] = data
        else:
            next_slot = self.rehash(slot)
            while self._slots[next_slot] is not None and self._slots[next_slot] != key:
                next_slot = self.rehash(next_slot)

            if self._slots[next_slot] is None:
                self._slots[next_slot] = key
                self._data[next_slot] = data
            else:
                self._data[next_slot] = data

    def hash(self, key):
        return key % self._size

    def rehash(self, old_hash):
        return (old_hash + 1) % self._size

    def get(self, key):
        data = None
        stop, found = False, False
        position = slot = self.hash(key)
        while self._slots[position] is not None and not found and not stop:
            if self._slots[position] == key:
                found = True
                data = self._data[position]
            else:
                position = self.rehash(position)
                if position == slot:
                    stop = True
        return data

    def delete(self, key):
        data = self.get(key)
        if data is not None:
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
