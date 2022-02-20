base = int(input())
tablesize = int(input())
string = input()

lenght = len(string)
print(sum([base ** (lenght - pos - 1) * ord(char) for pos, char in enumerate(string)]) % tablesize)
