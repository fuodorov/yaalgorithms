class CustomNoItemsException(Exception):
    def __init__(self):
        pass


class CustomOverflowException(Exception):
    def __init__(self):
        pass


class MyQueueSized:
    def __init__(self, max_size):
        self.__array = [None] * max_size  # Список, реализующий очередь
        self.__max_size = max_size
        self.__head = 0  # Индекс начала
        self.__tail = -1  # Индекс конца
        self.__size = 0  # Размер очереди

    def push(self, element):
        if self.__size != self.__max_size:  # Если есть место
            self.__tail = (self.__tail + 1) % self.__max_size
            self.__array[self.__tail] = element  # то записываем новый элемент в конец
            self.__size += 1
        else:
            raise CustomOverflowException

    def size(self):
        return self.__size

    def peek(self):
        if self.__size == 0:
            raise CustomNoItemsException
        else:
            return self.__array[self.__head]

    def pop(self):
        x = self.peek()
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return x


n = int(input())
max_size = int(input())
sizedQueue = MyQueueSized(max_size)

for i in range(n):
    try:
        command = input().split(' ')
        if len(command) == 1:
            print(getattr(sizedQueue, command[0])())
        else:
            getattr(sizedQueue, command[0])(int(command[1]))
    except CustomOverflowException:
        print('error')
    except CustomNoItemsException:
        print('None')
