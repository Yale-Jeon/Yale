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
    start = []
    end = []
    n = len(logs)
    for log in logs:
        start.append(strtime(log.split('-')[0]))
        end.append(strtime(log.split('-')[1]))
    start.sort()
    end.sort()
    s_num = 0
    e_num = 0
    max_start = 0
    max_time = 0
    num = 0
    while True:
        if num == n:
            break
        if start[num] >= advtime:
            break
        max_time += long(0, advtime, start[num], end[num])
        num += 1
    while True:
        if s_num == n or e_num == n:
            break
        if start[s_num] < end[e_num]:
            t = start[s_num]
            num = e_num
            result = 0
            while True:
                if num == n:
                    break
                if start[num] >= t + advtime:
                    break
                result += long(t, t + advtime, start[num], end[num])
                num += 1
            if result > max_time:
                max_time = result
                max_start = t
            s_num += 1
        else:
            t = end[e_num]
            e_num += 1
            num = e_num
            result = 0
            while True:
                if num == n:
                    break
                if start[num] >= t + advtime:
                    break
                result += long(t, t + advtime, start[num], end[num])
                num += 1
            if result > max_time:
                max_time = result
                max_start = t
        if t >= playtime - advtime:
            break

    s_num = 0
    e_num = 0
    while True:
        if s_num == n or e_num == n:
            break
        if start[s_num] < end[e_num]:
            t = start[s_num]
            if t < advtime:
                s_num += 1
                continue
            num = s_num
            result = 0
            while True:
                if num == -1:
                    break
                if end[num] <= t - advtime:
                    break
                result += long(t - advtime, t, start[num], end[num])
                num -= 1
            if result > max_time:
                max_time = result
                max_start = t
            s_num += 1
        else:
            t = end[e_num]
            if t < advtime:
                e_num += 1
                continue
            e_num += 1
            num = s_num
            result = 0
            while True:
                if num == -1:
                    break
                if end[num] <= t - advtime:
                    break
                result += long(t - advtime, t, start[num], end[num])
                num -= 1
            if result > max_time:
                max_time = result
                max_start = t
        if t >= playtime:
            break

    answer = inverse_time(max_start)

    return answer