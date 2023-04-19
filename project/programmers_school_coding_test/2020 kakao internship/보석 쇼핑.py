from collections import defaultdict

def solution(gems):
    answer = []
    c_table = defaultdict(lambda: 0)
    min_long = 99999
    n_gems = len(set(gems))
    n = len(gems)
    start = 0
    end = n_gems - 1
    long = end - start
    for i in range(end + 1):
        c_table[gems[i]] += 1
    while end < n and start <= n - n_gems:
        if len(c_table) < n_gems:
            if end == n - 1:
                break
            end += 1
            long += 1
            c_table[gems[end]] += 1
        else:
            if long < min_long:
                min_long = long
                answer = [start + 1, end + 1]
            c_table[gems[start]] -= 1
            if c_table[gems[start]] == 0:
                del (c_table[gems[start]])
            start += 1
            long -= 1

    return answer