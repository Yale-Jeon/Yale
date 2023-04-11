def correct(q):
    d = 0
    for i in range(len(q)):
        if q[i] == '(':
            d += 1
        else:
            if d == 0:
                return False
            else:
                d -= 1
    return d == 0


def balance(q):
    if q.count('(') == 0.5 * len(q):
        return True
    return False


def reverse(q):
    result = ''
    for x in q[1:-1]:
        if x == '(':
            result += ')'
        else:
            result += '('
    return result


def solution(p):
    if correct(p):
        return p
    if p == ')(':
        return '()'
    answer = ''
    i = 0
    d = 0
    u = ''
    while True:
        u += p[i]
        if p[i] == '(':
            d += 1
        else:
            d -= 1
        i += 1
        if d == 0:
            break

    v = p[i:]
    if correct(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse(u)

    return answer