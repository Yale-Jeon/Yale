def multiple(lst1, lst2):
    if lst1 == []:
        return lst2
    ret = []
    for l1 in lst1:
        for l2 in lst2:
            ret.append(l1 + l2)
    return ret


def solution(info, query):
    answer = []
    lst = []
    d = {'cpp': 0, 'java': 8, 'python': 16, 'backend': 0, 'frontend': 4, 'junior': 0, 'senior': 2, 'chicken': 0,
         'pizza': 1}
    dd = {0: [0, 8, 16], 1: [0, 4], 2: [0, 2], 3: [0, 1]}
    app = {}
    for i in range(24):
        app[i] = []
    for data in info:
        x = data.split(' ')
        tmp = 0
        for i in range(len(x) - 1):
            tmp += d[x[i]]
        app[tmp].append(int(x[-1]))

    for q in query:
        x = q.split(' and ')
        y = x[-1].split(' ')
        condition = x[:-1] + [y[0]]
        n = int(y[1])
        cnt = 0
        ret = []
        for c in range(len(condition)):
            if condition[c] == '-':
                tmp = dd[c]
                ret = multiple(ret, tmp)
            else:
                tmp = [d[condition[c]]]
                ret = multiple(ret, tmp)
        for r in ret:
            for a in app[r]:
                if a >= n:
                    cnt += 1
        answer.append(cnt)

    return answer