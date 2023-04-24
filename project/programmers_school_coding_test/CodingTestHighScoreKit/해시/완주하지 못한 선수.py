from collections import Counter
def solution(participant, completion):
    c = Counter(participant) - Counter(completion)
    for x in c:
        if c[x] > 0:
            return x