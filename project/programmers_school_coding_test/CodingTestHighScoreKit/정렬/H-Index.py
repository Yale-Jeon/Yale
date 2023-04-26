from collections import Counter
def solution(citations):
    n = len(citations)
    counter = Counter(citations)
    c = 0
    h = 0
    while True:
        if n-c < h:
            break
        if h in counter:
            c += counter[h]
        h += 1
    return h-1