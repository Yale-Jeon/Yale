def solution(n, arr1, arr2):
    answer = []
    a1 = []
    a2 = []
    for i in range(n):
        x = []
        y = arr1[i]
        for j in range(n):
            if y >= 2:
                x.insert(0, y % 2)
                y = (y - y % 2) / 2
            else:
                x.insert(0, y % 2)
                y = 0
        a1.append(x)
    for i in range(n):
        x = []
        y = arr2[i]
        for j in range(n):
            if y >= 2:
                x.insert(0, y % 2)
                y = (y - y % 2) / 2
            else:
                x.insert(0, y % 2)
                y = 0
        a2.append(x)

    for i in range(n):
        x = ''
        for j in range(n):
            if a1[i][j] == 0 and a2[i][j] == 0:
                x += ' '
            else:
                x += '#'
        answer.append(x)
    return answer