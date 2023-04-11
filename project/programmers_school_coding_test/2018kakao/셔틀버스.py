def change(result):
    a = str(result // 60)
    b = str(result % 60)
    if len(a) < 2:
        a = '0' + a
    if len(b) < 2:
        b = '0' + b
    return (a + ":" + b)


def solution(n, t, m, timetable):
    time = []
    bus = []
    x = len(timetable)
    for i in timetable:
        time.append(int(i[0:2]) * 60 + int(i[3:5]))
    time.sort()
    for i in range(n):
        bus.append(540 + t * i)

    last_bus = bus[-1]
    last_man = -1
    last_full = False
    for i in range(n):
        man = 0
        for j in range(m):
            if len(time) == 0:
                last_full = False
            elif time[0] <= bus[i]:
                last_man = time.pop(0)
                man += 1
                if i == n - 1 and man == m:
                    last_full = True
    if last_full:
        result = last_man - 1
    else:
        result = last_bus

    answer = change(result)
    return answer