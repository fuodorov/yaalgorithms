class NoItemsException(Exception):
    def __init__(self):
        pass
        

class MaxItemsException(Exception):
    def __init__(self):
        pass


class Deck:
    def __init__(self, max_size):
        self._array = [None] * max_size
        self._max_size = max_size
        self._size = 0
        self._head = 0
        self._tail = -1

    @property
    def is_full(self):
        return self._size == self._max_size

    @property
    def is_empty(self):
        return self._size == 0

    def push_back(self, value):
        if self.is_full:
            raise MaxItemsException
        else:
            self._tail = (self._tail + 1) % self._max_size
            self._array[self._tail] = value
            self._size += 1

    def push_front(self, value):
        if self.is_full:
            raise MaxItemsException
        else:
            self._head = (self._head - 1) % self._max_size
            self._array[self._head] = value
            self._size += 1

    def pop_back(self):
        if self.is_empty:
            raise NoItemsException
        else:
            value = self._array[self._tail]
            self._tail = (self._tail - 1) % self._max_size
            self._size -= 1
            return value

    def pop_front(self):
        if self.is_empty:
            raise NoItemsException
        else:
            value = self._array[self._head]
            self._head = (self._head + 1) % self._max_size
            self._size -= 1
            return value


n = int(input())
m = int(input())

deck = Deck(m)

for _ in range(n):
    try:
        cmd = input().split(' ')
        if len(cmd) == 1:
            print(getattr(deck, cmd[0])())
        else:
            getattr(deck, cmd[0])(cmd[1])
    except NoItemsException:
        print('error')
    except MaxItemsException:
        print('error')
