import collections

def solution(gems):
    answer = []
    i=0
    d = {}
    min_long=99999
    lst = collections.Counter(gems)
    for l in lst:
        d[l]=i
        i += 1
    ld = len(d)
    c_table = [0]*ld
    n = len(gems)
    start=0
    end=len(d)-1
    long = end-start
    for i in range(end+1):
        c_table[d[gems[i]]] += 1
    while end < n and start <= n-ld:
        if 0 in c_table:
            if end == n-1:
                break
            end += 1
            long += 1
            c_table[d[gems[end]]] += 1
        else:
            if long < min_long:
                min_long = long
                answer = [start+1,end+1]
            c_table[d[gems[start]]] -= 1
            start += 1
            long -= 1

    return answer