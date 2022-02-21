base = int(input())
tablesize = int(input())
string = input()


def polynomial_hash(str, p, m):
    power_of_p = 1
    hash_val = 0

    for char in str:
        hash_val = (hash_val + ord(char) * power_of_p) % m
        power_of_p = (power_of_p * p) % m

    return hash_val


for i in range(int(input())):
    l, r = input().split()
    print(polynomial_hash(reversed(string[int(l)-1:int(r)]), base, tablesize))
