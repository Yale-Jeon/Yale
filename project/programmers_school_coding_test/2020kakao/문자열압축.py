def f(d):
    a = 1
    while True:
        if d < 10:
            break
        else:
            d = d / 10
            a += 1
    return a


def solution(s):
    n = len(s)
    answer = n
    for i in range(1, int(n / 2) + 1):
        a = 0
        b = n % i
        c = ''
        d = 1
        for j in range(int(n / i)):
            if j == 0:
                c = s[i * j:i * (j + 1)]
            else:
                if s[i * j:i * (j + 1)] == c:
                    d += 1
                else:
                    if d == 1:
                        a += 1
                    else:
                        a += 1
                        b += f(d)
                        d = 1
                    c = s[i * j:i * (j + 1)]

        if d == 1:
            a += 1
        else:
            a += 1
            b += f(d)
            d = 1
        answer = min(answer, a * i + b)

    return answer