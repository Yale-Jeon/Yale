# 실제 list를 작성하여 동일한 과정 실행
def solution(n, k, cmd):  # 현재위치, 삭제기록 lst(index), 복구시 index와 현재위치를 비교하여 현재위치 변경
    lst = [i for i in range(n)]  # 가상 list 0~n-1
    answer = ''
    del_list = []  # [[value, index]]
    now = k
    del_len = 0
    for c in cmd:
        command = c.split()[0]
        if command == 'U':
            now -= int(c.split()[1])
        elif command == 'D':
            now += int(c.split()[1])
        elif command == 'C':  # 삭제
            if now == n - 1 - del_len:  # 마지막 행
                del_list.append([lst.pop(-1), now])
                now -= 1
            else:
                del_list.append([lst.pop(now), now])
            del_len += 1
        else:  # Z
            r = del_list.pop(-1)
            if r[1] <= now:
                lst.insert(r[1], r[0])
                now += 1
            else:
                lst.insert(r[1], r[0])
            del_len -= 1

    i = 0
    for j in range(n):
        if i == n - del_len:
            answer += 'X'
        else:
            if lst[i] == j:
                answer += 'O'
                i += 1
            else:
                answer += 'X'

    return answer

# 실제 list 없이 del_list만을 사용
def solution(n, k, cmd):  # 현재위치, 삭제기록 lst(index), 복구시 index와 현재위치를 비교하여 현재위치 변경
    answer = ''
    del_list = []  # [index]
    now = k
    now_move = 0
    del_len = 0
    last = n - 1
    for c in cmd:
        command = c.split()[0]
        if command == 'U':
            now_move -= int(c.split()[1])
        elif command == 'D':
            now_move += int(c.split()[1])
        elif command == 'C':  # 삭제
            # 이동처리
            if now_move > 0:
                while now_move != 0:
                    now += 1
                    if now not in del_list:
                        now_move -= 1
            elif now_move < 0:
                while now_move != 0:
                    now -= 1
                    if now not in del_list:
                        now_move += 1
            # 제거
            if now == last:  # 마지막 행
                del_list.append(now)
                last -= 1
                now -= 1
                while True:
                    if now in del_list:
                        now -= 1
                    else:
                        break
            else:
                del_list.append(now)
                now += 1
                while True:
                    if now in del_list:
                        now += 1
                    else:
                        break
            del_len += 1
        else:  # Z
            # 이동처리
            if now_move > 0:
                while now_move != 0:
                    now += 1
                    if now not in del_list:
                        now_move -= 1
            elif now_move < 0:
                while now_move != 0:
                    now -= 1
                    if now not in del_list:
                        now_move += 1
            # 복원
            r = del_list.pop(-1)
            if r > last:
                last += 1
            del_len -= 1

    del_list.sort()
    if del_len == 0:
        return 'O' * n
    i = 0
    for d in del_list:
        answer += 'O' * (d - i)
        answer += 'X'
        i = d + 1
    answer += 'O' * (n - i)

    return answer

# 두 방식 모두 정확성은 통과하나 효율성에서 탈락함