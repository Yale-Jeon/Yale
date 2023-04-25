import math
def solution(progresses, speeds):
    answer = []
    if len(progresses)==1: return [1]
    lst = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(len(progresses))]
    last = lst[0]
    c = 0
    for l in lst:
        if l > last:
            answer.append(c)
            last = l
            c = 1
        else:
            c += 1
    answer.append(c)
    return answer