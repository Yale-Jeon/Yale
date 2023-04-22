# dijkstar  q에 넣을때 이전 움직임 가로,세로를 넣어 반대되는 움직임시 cost 500 추가 시작지점이0,0이니 처음 q에 1,0,세로, 0,1, 가로 2개를 넣고 시작
import heapq

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

def solution(board):  # 단순 distance만 썼을 때 distance[x][y]에 어느방향에서 접근했는지에 대한 정보가 남아있지 않음
    n = len(board)
    answer = 0
    distance0 = [[999999 for i in range(n)] for i in range(n)] # 마지막에세로에서 x,y까지 갔을때 거리
    distance1 = [[999999 for i in range(n)] for i in range(n)] # 마지막에가로에서 x,y까지 갔을때 거리
    distance0[0][0] = 0  # 시작위치
    distance1[0][0] = 0  # 시작위치
    q = []
    if board[1][0] == 0:
        heapq.heappush(q, (100, 1, 0, 0))
        distance0[1][0] = 100
    if board[0][1] == 0:
        heapq.heappush(q, (100, 0, 1, 1))
        distance1[0][1] = 100
    while q:
        now_dist, x, y, pre_d = heapq.heappop(q)
        if pre_d == 0:
            if distance0[x][y] < now_dist:
                continue
        else:
            if distance1[x][y] < now_dist:
                continue
        for new_x, new_y, new_d in next_city(x, y, n):
            if board[new_x][new_y] == 0:
                d = 0
                if pre_d != new_d:
                    d = 500
                cost = now_dist + 100 + d
                if new_d == 0:
                    if cost <= distance0[new_x][new_y]:
                        distance0[new_x][new_y] = cost
                        heapq.heappush(q, (cost, new_x, new_y, new_d))
                else:
                    if cost <= distance1[new_x][new_y]:
                        distance1[new_x][new_y] = cost
                        heapq.heappush(q, (cost, new_x, new_y, new_d))
    answer = min(distance0[n - 1][n - 1],distance1[n - 1][n - 1])

    return answer