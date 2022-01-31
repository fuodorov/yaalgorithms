class CustomNoItemsException(Exception):
    def __init__(self):
        pass


class QueueUsingList:
    def __init__(self):
        self.__array = []  # Список, реализующий очередь

    def put(self, element):
        self.__array.append(element)

    def size(self):
        return len(self.__array)

    def get(self):
        if self.size() == 0:
            raise CustomNoItemsException
        else:
            return self.__array.pop(0)


n = int(input())
queueUsingList = QueueUsingList()

for i in range(n):
    try:
        command = input().split(' ')
        if len(command) == 1:
            print(getattr(queueUsingList, command[0])())
        else:
            getattr(queueUsingList, command[0])(command[1])
    except CustomNoItemsException:
        print('error')
