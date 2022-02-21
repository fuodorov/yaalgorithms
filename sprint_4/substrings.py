def longest_without_duplication(s):
    max_s = ''
    cnt = 0
    max_cnt = 0
    begin, end = 0, len(s)-1
    
    while begin <= end:
        if s[begin] not in max_s:
            max_s += s[begin]
            cnt += 1
        else:
            index = max_s.index(s[begin])
            max_s = max_s[max_s.index(s[begin]) + 1:] + s[begin]
            cnt = len(max_s)

        if cnt > max_cnt:
            max_cnt = cnt

        begin += 1

    return max_cnt


print(longest_without_duplication(input()))
