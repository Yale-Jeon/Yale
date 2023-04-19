def go(board, start, end):
    if start == end:
        return 0

    if start[0] == end[0]:
        if abs(end[1] - start[1]) == 1:
            return 1
        if start[1] < end[1]:
            last = -1
            cnt = 0
            for i in range(start[1], end[1]):
                if board[start[0]][i + 1] != 0:
                    cnt += 1
                last = board[start[0]][i + 1]
            if abs(start[1] - end[1]) == 2 and cnt == 0:
                return 2
            if last == 0:
                cnt += 1
            return cnt
        else:
            last = -1
            cnt = 0
            for i in range(start[1], end[1], -1):
                if board[start[0]][i - 1] != 0:
                    cnt += 1
                last = board[start[0]][i - 1]
            if abs(start[1] - end[1]) == 2 and cnt == 0:
                return 2
            if last == 0:
                cnt += 1
            return cnt

    if start[1] == end[1]:
        if abs(end[0] - start[0]) == 1:
            return 1
        if start[0] < end[0]:
            last = -1
            cnt = 0
            for i in range(start[0], end[0]):
                if board[i + 1][start[1]] != 0:
                    cnt += 1
                last = board[i + 1][start[1]]
            if abs(start[0] - end[0]) == 2 and cnt == 0:
                return 2
            if last == 0:
                cnt += 1
            return cnt
        else:
            last = -1
            cnt = 0
            for i in range(start[0], end[0], -1):
                if board[i - 1][start[1]] != 0:
                    cnt += 1
                last = board[i - 1][start[1]]
            if abs(start[0] - end[0]) == 2 and cnt == 0:
                return 2
            if last == 0:
                cnt += 1
            return cnt

    result = []
    if start[0] < end[0]:
        for i in range(start[0], end[0]):
            result.append(go(board, start, [i + 1, start[1]]) + go(board, [i + 1, start[1]], end))
    else:
        for i in range(start[0], end[0], -1):
            result.append(go(board, start, [i - 1, start[1]]) + go(board, [i - 1, start[1]], end))

    if start[1] < end[1]:
        for i in range(start[1], end[1]):
            result.append(go(board, start, [start[0], i + 1]) + go(board, [start[0], i + 1], end))
    else:
        for i in range(start[1], end[1], -1):
            result.append(go(board, start, [start[0], i - 1]) + go(board, [start[0], i - 1], end))

    return min(result)


def eliminate(board, r, c, lst, dic):
    if len(lst) == 0:
        return 0
    result = []
    for card in lst:
        c1, c2 = dic[card][0], dic[card][1]
        route1 = (go(board, [r, c], c1) + go(board, c1, c2))
        route2 = (go(board, [r, c], c2) + go(board, c2, c1))
        lst2 = lst[::]
        lst2.remove(card)
        board2 = board[::]
        board2[c1[0]][c1[1]] = 0
        board2[c2[0]][c2[1]] = 0

        r1 = 2 + route1 + eliminate(board2, c2[0], c2[1], lst2, dic)
        r2 = 2 + route2 + eliminate(board2, c1[0], c1[1], lst2, dic)
        result.append(min(r1, r2))
    return min(result)


def solution(board, r, c):
    answer = 0
    dic = {}  # key: 카드번호, value: 좌표
    # dic = {1:[[x,y],[x2,y2]], 3: ...}
    for x in range(4):
        for y in range(4):
            if board[x][y] != 0:
                if board[x][y] not in dic:
                    dic[board[x][y]] = [[x, y]]
                else:
                    dic[board[x][y]].append([x, y])

    lst = list(dic.keys())  # 남은카드목록
    answer = eliminate(board, r, c, lst, dic)

    return answer