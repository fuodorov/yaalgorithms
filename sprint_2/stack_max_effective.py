class StackMaxEffective:
    def __init__(self):
        self.stack_ = []

    def __bool__(self):
        return bool(self.stack_)

    def push(self, item):
        if self.stack_:
            new_max = max(item, self.stack_[-1][1])
        else:
            new_max = item
        self.stack_.append((item, new_max))

    def pop(self):
        return self.stack_.pop()[0]

    def get_max(self):
        return self.stack_[-1][1]


s = StackMaxEffective()

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'pop':
        if s:
            s.pop()
        else:
            print('error')
    if cmd[0] == 'push':
        s.push(int(cmd[1]))
    if cmd[0] == 'get_max':
        if s:
            print(s.get_max())
        else:
            print('None')