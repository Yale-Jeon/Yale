from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for route in permutations(dungeons, len(dungeons)):
        temp = k
        c = 0
        for d in route:
            if temp >= d[0]:
                temp -= d[1]
                c += 1
            else:
                break
        if c > answer:
            answer = c
    return answer