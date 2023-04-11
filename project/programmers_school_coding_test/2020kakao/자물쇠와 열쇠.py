def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    d = []
    locks = []
    home = 0
    dol = 0

    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                d.append([i, j])
                dol += 1

    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                locks.append([i, j])
                home += 1

    if home == 0:
        return True
    if dol < home:
        return False

    keys = [d, [], [], []]
    for dd in d:
        y, x = dd[0], dd[1]
        keys[1].append([x, m - 1 - y])
        keys[2].append([m - 1 - y, m - 1 - x])
        keys[3].append([m - 1 - x, y])

    for k in keys:
        for i in range(len(k)):
            a, b = locks[0][0] - k[i][0], locks[0][1] - k[i][1]
            cnt = 0
            for j in range(len(k)):
                if k[j][0] + a in range(0, n) and k[j][1] + b in range(0, n):
                    if [k[j][0] + a, k[j][1] + b] in locks:
                        cnt += 1
                    else:
                        break
            if cnt == home:
                return True

    return answer