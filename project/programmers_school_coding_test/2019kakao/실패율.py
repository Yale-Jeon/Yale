def solution(N, stages):
    answer = []
    c = len(stages)
    a = []
    for i in range(N + 2):
        a.append(0)

    fail_rate = []
    for stage in stages:
        a[int(stage)] += 1

    b = 0
    for j in range(N + 1):
        if b == c:
            fail_rate.append(0)
        else:
            fail_rate.append(a[j] / (c - b))
            b += a[j]

    for k in range(N):
        i = 0
        while i < len(answer):
            if fail_rate[k + 1] > fail_rate[answer[i]]:
                break
            else:
                i += 1
        answer.insert(i, k + 1)

    return answer