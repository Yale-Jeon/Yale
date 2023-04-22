def solution(places):
    answer = []
    for t in range(5): # 각 대기실 방문
        error = 1
        #가로확인
        for i in range(5):
            if 'PP' in places[t][i] or 'POP' in places[t][i]:
                error = 0
                break
        #세로확인
        for i in range(5):
            new = ''
            for j in range(5):
                new += places[t][j][i]
            if 'PP' in new or 'POP' in new:
                error = 0
                break
        #대각확인1 좌상->우하 0->4, 0->4
        for i in range(4): # 모든 자리 방문
            if error == 0:
                break
            for j in range(4): 
                if places[t][i][j] == 'P' and places[t][i+1][j+1] == 'P': # 각 학생 방문
                    if places[t][i+1][j] != 'X' or places[t][i][j+1] != 'X':
                        error = 0
                        break
        #대각확인2 우상->좌하 1->5, 0->4
        for i in range(4): # 모든 자리 방문
            if error == 0:
                break
            for j in range(1,5): 
                if places[t][i][j] == 'P' and places[t][i+1][j-1] == 'P': # 각 학생 방문
                    if places[t][i+1][j] != 'X' or places[t][i][j-1] != 'X':
                        error = 0
                        break
        answer.append(error)
    return answer