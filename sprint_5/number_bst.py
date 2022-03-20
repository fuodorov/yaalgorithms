# (2n)! / n! * (n+1)!

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

n = int(input())

print(int(fac(2*n)/(fac(n)*fac(n+1))))