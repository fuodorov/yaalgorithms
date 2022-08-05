#Python

def hashes_arr(b):
    s_len = len(b) + 1
    hashes = [0] * s_len
    hashes[1] = b[0]
    for i in range(2, s_len):
        hashes[i] = (hashes[i-1] * a + b[i-1]) % m
    return hashes

def fast_pow(x, p, r):
    m = x % r
    t = 1
    while p:
        if p % 2:
            t *= m
            t %= r
        m *= m
        m %= r
        p //= 2
    return t % r

a = int(input().strip())
m = int(input().strip())
hashes = hashes_arr(bytes(input().strip(), encoding='ascii'))
n = int(input().strip())

res = [0]*n
for i in range(n):
    s, e = input().strip().split()
    start, end = int(s), int(e)
    res[i] = (hashes[end] % m - hashes[start-1] * fast_pow(a, end- start + 1, m)) % m
print(*res, sep='\n')

