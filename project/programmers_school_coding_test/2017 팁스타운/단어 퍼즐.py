# 힙큐 안쓰는 버전
def solution(strs, t):
    d = {}
    q = [(0,'')]
    while q:
        c, x = q.pop(0)
        if x in d and d[x] <= c:
            continue
        else:
            d[x] = c
        if x == t:
            continue
        for s in strs:
            if s == t[len(x):len(x)+len(s)]:
                q.append((c+1, x+s))
    if t not in d:
        return -1
    return d[t]


#힙큐 쓰는 버전
import heapq

def solution(strs, t):
    d = {}
    q = []
    heapq.heappush(q, (0, ''))
    while q:
        c, x = heapq.heappop(q)
        if x in d and d[x] <= c:
            continue
        else:
            d[x] = c

        for s in strs:
            if s == t[len(x):len(x) + len(s)]:
                if x+s == t:
                    return c+1
                heapq.heappush(q, (c + 1, x + s))
    return -1