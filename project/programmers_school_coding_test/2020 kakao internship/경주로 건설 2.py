# 경주로 건설을 recursion으로 해결하기

def next_city(x, y, n):  # x,y는 지금위치
    lst = []
    if x == 0:
        xlst = [1]
    elif x == n - 1:
        xlst = [n - 2]
    else:
        xlst = [x - 1, x + 1]
    if y == 0:
        ylst = [1]
    elif y == n - 1:
        ylst = [n - 2]
    else:
        ylst = [y - 1, y + 1]
    for i in xlst:
        lst.append([i, y, 0])
    for j in ylst:
        lst.append([x, j, 1])
    return lst  # lst = [[x,y,d(d is pre direction)]....] lst원소들을 q에 넣을예정 d=0 세로, d=1 가로

def recursion(x, y, d, n, visited, board, cost):  # x,y는 지금위치
    if x==n-1 and y==n-1:
        return [cost]
    result = []
    nextcity = next_city(x, y, n)
    new_visited = visited[::]
    for nx, ny, nd in nextcity:
        if [nx, ny] not in visited and board[nx][ny] == 0:
            new_visited += [[nx, ny]]
    for nx, ny, nd in nextcity:
        if [nx, ny] not in visited and board[nx][ny] == 0:
            if d == nd:
                new_cost = 100
            else:
                new_cost = 600
            if d == -1:
                new_cost = 100
            result += recursion(nx, ny, nd, n, new_visited, board, cost + new_cost)
    return result

def solution(board):  # 초기d= -1
    n = len(board)
    answer = min(recursion(0,0,-1,n,[[0,0]], board, 0))
    return answer

#board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
#print(solution(board))

# 문제: 런타임에러 (시간초과). 결과는 맞음.
