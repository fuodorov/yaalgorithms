base = int(input())
tablesize = int(input())
string = input()


def polynomial_hash(str, p, m):
    power_of_p = 1
    hash_val = 0

    for char in str:
        hash_val = ((hash_val + ord(char) * power_of_p) % m)
        power_of_p = (power_of_p * p) % m
 
    return int(hash_val)

print(polynomial_hash(string[::-1], base, tablesize))
