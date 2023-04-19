def strtime(str_time):
    h, m, s = str_time.split(':')
    return 3600 * int(h) + 60 * int(m) + int(s)


def inverse_time(int_time):
    s = int_time % 60
    m = (int_time - s) / 60 % 60
    h = int_time // 3600
    if s < 10:
        s = '0' + str(s)
    else:
        s = str(s)
    if m < 10:
        m = '0' + str(int(m))
    else:
        m = str(int(m))
    if h < 10:
        h = '0' + str(h)
    else:
        h = str(h)
    return h + ':' + m + ':' + s


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
    start = []
    end = []
    n = len(logs)
    for log in logs:
        start.append(strtime(log.split('-')[0]))
        end.append(strtime(log.split('-')[1]))
    start.sort()
    end.sort()
    lst = []
    t_max = playtime - advtime
    for s in start:
        if s <= t_max:
            lst.append(s)
        if s > advtime:
            lst.append(s - advtime)
    for e in end:
        if e <= t_max:
            lst.append(e)
        if e > advtime:
            lst.append(e - advtime)

    max_start = 0
    max_time = 0
    str_num = 0

    current = []
    while True:
        if str_num == n:
            break
        if start[str_num] < advtime:
            current.append(str_num)
            str_num += 1
        else:
            break
    for c in current:
        max_time += long(0, advtime, start[c], end[c])

    for t in lst:
        result = 0
        while True:
            if str_num == n:
                break
            if start[str_num] < t + advtime:
                current.append(str_num)
                str_num += 1
            else:
                break
        while True:
            if len(current) == 0:
                break
            if end[current[0]] <= t:
                current.pop(0)
            else:
                break
        for c in current:
            result += long(t, t + advtime, start[c], end[c])
        if result > max_time:
            max_time = result
            max_start = t

    answer = inverse_time(max_start)

    return answer