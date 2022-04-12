def is_same_amounts(cnt_elem, mass_elems):
    sum_elems = sum(mass_elems)
    if sum_elems % 2 != 0:
        return False

    half_sum = sum_elems // 2
    dp = [True] + [False] * half_sum
    for i in range(1, cnt_elem+1):
        for j in range(half_sum, mass_elems[i-1]-1, -1):
            dp[j] = dp[j-mass_elems[i-1]] or dp[j]
            if j == half_sum and dp[j]:
                return True
    return dp[-1]


print(is_same_amounts(int(input()), list(map(int, input().split()))))