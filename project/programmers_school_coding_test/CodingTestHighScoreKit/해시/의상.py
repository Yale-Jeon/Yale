from collections import defaultdict
def solution(clothes):
    d = defaultdict(lambda: 0)
    for cloth in clothes:
        d[cloth[1]] += 1
    answer = 0
    for x in d:
        if answer == 0:
            answer = d[x]+1
        else:
            answer *= d[x]+1
    return answer-1