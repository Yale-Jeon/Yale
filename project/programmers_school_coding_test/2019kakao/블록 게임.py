def is_clear(xy, board):
    for i in range(xy[1] + 1):
        if board[i][xy[0]] != 0:
            return False
    return True


def block(num, stack):
    a = stack[num]
    if a[0][1] == a[1][1]:
        return [-1]
    if a[1][1] + a[2][1] == a[0][1] + a[3][1]:
        return [-1]
    if a[0][0] == a[3][0] and a[0][1] + 1 == a[3][1]:
        return [(a[0][0] - 2, a[0][1]), (a[0][0] - 1, a[0][1])]
    if a[0][0] == a[3][0] and a[0][1] + 2 == a[3][1]:
        return [(a[0][0] - 1, a[0][1]), (a[0][0] - 1, a[0][1] + 1)]
    if a[0][0] + 2 == a[3][0] and a[0][1] + 1 == a[3][1]:
        return [(a[0][0] + 1, a[0][1]), (a[0][0] + 2, a[0][1])]
    if a[0][0] + 1 == a[3][0] and a[0][1] + 2 == a[3][1]:
        return [(a[0][0] + 1, a[0][1]), (a[0][0] + 1, a[0][1] + 1)]
    if a[0][0] + 1 == a[3][0] and a[0][1] + 1 == a[3][1]:
        return [(a[0][0] - 1, a[0][1]), (a[0][0] + 1, a[0][1])]
    else:
        print("error")
        return [-1]


def solution(board):
    answer = 0
    stack = {}
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != 0:
                if board[y][x] not in stack:
                    stack[board[y][x]] = [(x, y)]
                else:
                    stack[board[y][x]].append((x, y))

    cc = 1
    while cc != 0:
        cc = 0
        delete = []
        for s in stack.keys():
            a = block(s, stack)
            if len(a) == 2:
                if is_clear(a[0], board) and is_clear(a[1], board):
                    for i in stack[s]:
                        board[i[1]][i[0]] = 0
                    delete.append(s)
                    answer += 1
                    cc += 1
        for s in delete:
            del stack[s]

    return answer