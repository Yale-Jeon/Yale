def solution(prices):
    lst = []
    n = len(prices)
    answer = [0] * n
    for i, p in enumerate(prices):
        if len(lst) == 0:
            lst.append(i)
        else:
            removelst = []
            for j in lst:
                if prices[j] > p:
                    answer[j] = i - j
                    removelst.append(j)
            for r in removelst:
                lst.remove(r)
            lst.append(i)

    for i in lst:
        answer[i] = n - 1 - i

    return answer