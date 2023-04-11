def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        k = []
        for j in board[i]:
            k.append(j)
        board[i] = k
    while True:
        del_list = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    if board[i][j] != '1':
                        del_list.append((i, j))
        if len(del_list) == 0:
            break
        for d in del_list:
            board[d[0]][d[1]] = '1'
            board[d[0] + 1][d[1]] = '1'
            board[d[0]][d[1] + 1] = '1'
            board[d[0] + 1][d[1] + 1] = '1'
        while True:
            c = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] != '1' and board[i + 1][j] == '1':
                        board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                        c = 1
            if c == 0:
                break
        answer = 0
        for i in board:
            answer += i.count('1')

    return answer