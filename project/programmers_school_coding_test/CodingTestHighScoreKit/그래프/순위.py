def solution(n, results):
    answer = 0
    weak = {}
    strong = {}
    for i in range(n):
        weak[i + 1] = []
        strong[i + 1] = []
    for s, w in results:
        weak[s].append(w)
        strong[w].append(s)

    c = 1
    while c == 1:
        c = 0
        for i in range(1, n + 1):
            for w in weak[i]:
                for ww in weak[w]:
                    if ww not in weak[i]:
                        weak[i].append(ww)
                        c = 1
            for s in strong[i]:
                for ss in strong[s]:
                    if ss not in strong[i]:
                        strong[i].append(ss)
                        c = 1

    for i in range(1, n + 1):
        if len(weak[i]) + len(strong[i]) == n - 1:
            answer += 1

    return answer