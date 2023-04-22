from collections import defaultdict

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

def solution(play_time, adv_time, logs):
    playtime = strtime(play_time)
    advtime = strtime(adv_time)
    lst = defaultdict(lambda: 0)
    n = len(logs)
    for log in logs:
        for i in range(strtime(log.split('-')[0]), strtime(log.split('-')[1])):
            lst[i] += 1
    total = 0
    for i in range(advtime):
        total += lst[i]
    max_start = 0
    max_time = total
    for i in range(1, playtime-advtime+1):
        total -= lst[i-1]
        total += lst[i+advtime-1]
        if total > max_time:
            max_time = total
            max_start = i
    answer = inverse_time(max_start)

    return answer