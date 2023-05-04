def solution(routes):
    routes.sort()
    answer = 0
    i = 0
    while len(routes)>0:
        start, end = routes.pop(i)
        while i <= len(routes)-1:
            s, e = routes[i]
            if start <= e and e <= end:
                end = e
                routes.pop(i)
            elif s <= end and end <= e:
                start = s
                routes.pop(i)
            else:
                break
        answer += 1

    return answer