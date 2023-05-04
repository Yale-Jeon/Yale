def solution(line):
    answer = []
    n = len(line)
    star = []
    xstart = 1000000000000000000
    xend = -1000000000000000000
    ystart = 1000000000000000000
    yend = -1000000000000000000
    for i in range(n):
        for j in range(i + 1, n):
            a1, b1, c1 = line[i]
            a2, b2, c2 = line[j]
            d = b2 * a1 - b1 * a2
            if d != 0:  # 평행인가?
                x, y = (b1 * c2 - b2 * c1) / d, (c1 * a2 - a1 * c2) / d
                if x == int(x) and y == int(y):
                    x, y = int(x), int(y)
                    star.append([x, y])
                    xstart, xend, ystart, yend = min(xstart, x), max(xend, x), min(ystart, y), max(yend, y)

    for j in range(yend + 1 - ystart):
        answer.append(['.' for i in range(xend + 1 - xstart)])
    for x, y in star:
        answer[yend - y][x - xstart] = '*'
    for j in range(yend - ystart + 1):
        answer[j] = ''.join(answer[j])

    return answer