import re


def music(string):
    if '#' not in string:
        return string
    d = {'C': 'c', 'D': 'd', 'F': 'f', 'G': 'g', 'A': 'a'}
    result = ''
    a, b = string.split('#')[:-1], string.split('#')[-1]
    for i in a:
        result += i[:-1] + d[i[-1]]
    result += b

    return result


def solution(m, musicinfos):
    lst = []
    melody = music(m)
    answer = ''
    i = 0
    for mm in musicinfos:
        a = mm.split(',')
        playtime = (int(a[1].split(':')[0]) - int(a[0].split(':')[0])) * 60 + (
                    int(a[1].split(':')[1]) - int(a[0].split(':')[1]))
        x = music(a[3])
        n = len(x)
        song = ''
        if n >= playtime:
            song = x[:playtime]
        else:
            song = x * (playtime // n) + x[:playtime % n]
        if melody in song:
            lst.append([a[2], playtime, i])
        i += 1

    if len(lst) == 0:
        return answer
    y = sorted(lst, key=lambda k: k[1], reverse=True)
    v = y[0][1]
    z = []
    for yy in y:
        if yy[1] == v:
            z.append(yy)
    answer = sorted(z, key=lambda k: k[2])[0][0]

    return answer