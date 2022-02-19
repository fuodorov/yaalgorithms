def is_subsequence(s, t):
    lens, lent = len(s), len(t)
    if lens == 0:
        return True

    if lens > lent:
        return False

    i = 0
    for j in range(lent):
        if s[i] == t[j]:
            i += 1
            if i == lens:
                return True

    return False


s = input()
t = input()
print(is_subsequence(s, t), end='')
