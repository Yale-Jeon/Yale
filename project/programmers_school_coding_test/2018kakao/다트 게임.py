import re

def solution(dartResult):
    answer = 0
    total_score = []
    a = re.findall('\d+', dartResult)
    b = re.sub('\d+', '.', dartResult).split('.')[1:]
    n = len(a)
    for i in range(n):
        score = int(a[i])

        if 'D' in b[i]:
            score = score * score
        elif 'T' in b[i]:
            score = score * score * score

        if '#' in b[i]:
            score = score * (-1)
        elif '*' in b[i]:
            score = score * 2
            if len(total_score) != 0:
                total_score[i - 1] = total_score[i - 1] * 2
        total_score.append(score)
    answer = sum(total_score)
    return answer