def levenshtein_distance(str_a, str_b):
    n, m = len(str_a), len(str_b)
    if n > m:
        str_a, str_b, n, m = str_b, str_a, m, n

    current_row = [i for i in range(n+1)]
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n+1):
            change = previous_row[j-1] + 1 if str_a[j-1] != str_b[i-1] else previous_row[j-1]
            current_row[j] = min(previous_row[j]+1, current_row[j-1]+1, change)
    return current_row[n]


print(levenshtein_distance(input(), input()))