def solution(n, weak, dist):
    dist.sort()
    m = len(weak)
    k = len(dist)
    if m == 0:
        return 0
    if k == 0:
        return 100
    if m == 1:
        return 1
    d = dist[-1]
    lst = []
    for i in range(m):
        v = []
        if weak[i] + d <= n:
            for j in range(m):
                if weak[j] < weak[i] or weak[j] > weak[i] + d:
                    v.append(weak[j])
        else:
            for j in range(m):
                if weak[j] < weak[i] and weak[j] > (weak[i] + d) % n:
                    v.append(weak[j])
        lst.append(1 + solution(n, v, dist[:-1]))
        v = []
        if weak[i] - d >= 0:
            for j in range(m):
                if weak[j] < weak[i] - d or weak[j] > weak[i]:
                    v.append(weak[j])
        else:
            for j in range(m):
                if weak[j] < (weak[i] - d) % n and weak[j] > weak[i]:
                    v.append(weak[j])
        lst.append(1 + solution(n, v, dist[:-1]))
    answer = min(lst)
    if answer >= 100:
        return -1

    return answer