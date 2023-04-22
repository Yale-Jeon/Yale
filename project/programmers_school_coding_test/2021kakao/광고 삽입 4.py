def strtime(str_time):
    h, m, s = str_time.split(':')
    return 3600 * int(h) + 60 * int(m) + int(s)


def inverse_time(int_time):
    s = int_time % 60
    m = (int_time - s) / 60 % 60
    h = int_time // 3600
    if s<10:
        s = '0'+str(s)
    if m<10:
        m = '0'+str(int(m))
    else:
        m = str(int(m))
    if h<10:
        h = '0'+str(h)
    return str(h) + ':' + m + ':' + str(s)


def long(adv_start, adv_end, start, end):
    if end <= adv_start:
        return 0
    if start >= adv_end:
        return 0
    if start < adv_start:
        if adv_end > end:
            return end - adv_start
        else:
            return adv_end - adv_start
    else:
        if adv_end < end:
            return adv_end - start
        else:
            return end - start


def solution(play_time, adv_time, logs):
    playtime = strtime(play_time)
    advtime = strtime(adv_time)
    time_table = []
    n = len(logs)
    for log in logs:
        time_table.append([strtime(log.split('-')[0]), strtime(log.split('-')[1])])
    time_table = sorted(time_table, key = lambda x:x[0])
    max_start = 0
    max_time = 0
    num = 0
    # 첫지점과 첫지점이 겹칠 때 algorithms
    while True: # start = 0일때 1회 실행
        if num == n:
            break
        if time_table[num][0] >= advtime:  # start가 광고 밖이라면
            break
        max_time += long(0, advtime, time_table[num][0], time_table[num][1])
        num += 1
    for i in range(n):
        start = time_table[i][0]
        if start > playtime - advtime:  # playtime-advtime에서 1회 실행하여야 하는가?
            break
        end = start + advtime
        total_time = 0
        for j in range(i,n): # 겹치는 광고부분 total_time에 모두 합함
            if time_table[j][0] < start + advtime:
                total_time += long(start, end, time_table[j][0], time_table[j][1])
            else:
                break
        if total_time > max_time:
            max_time = total_time
            max_start = start
    # 뒷지점과 뒷지점이 겹칠때 algorithms도 구현

    answer = inverse_time(max_start)

    return answer

# 시간초과 에러