def solution(s):
    s = list(s)
    lst = []

    for x in s:
        if len(lst) == 0 or lst[-1] != x:
            lst.append(x)
        else:
            lst.pop(-1)

    if len(lst) == 0:
        return 1
    else:
        return 0