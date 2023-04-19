def solution(numbers, hand):
    answer = ''
    d = {} # 0~9 좌표 dictionary
    for i in range(3):
        for j in range(3):
            d[3*i+j+1] = [i,j]
    d[0] = [3,1]
    LH = [3,0] # 현재 왼손 위치
    RH = [3,2] # 현재 오른손 위치
    for num in numbers:
        if num in [1,4,7]:
            LH = d[num]
            answer += 'L'
        elif num in [3,6,9]:
            RH = d[num]
            answer += 'R'
        else:
            x, y = d[num][0], d[num][1]
            distL = abs(x-LH[0])+abs(y-LH[1])
            distR = abs(x-RH[0])+abs(y-RH[1])
            if distL < distR:
                LH = d[num]
                answer += 'L'
            elif distL > distR:
                RH = d[num]
                answer += 'R'
            else:
                if hand == "left":
                    LH = d[num]
                    answer += 'L'
                else:
                    RH = d[num]
                    answer += 'R'
    return answer