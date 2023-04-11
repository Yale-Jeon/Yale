def radix(x, n, number):
    string = ''
    while True:
        if x >= n:
            string += number[x % n]
            x = x // n
        else:
            string += number[x]
            break
    return string[::-1]


def long(x, n):
    i = 1
    while True:
        if x < n ** i:
            return i
        else:
            i += 1


def solution(n, t, m, p):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    answer = ''
    string = ''
    i = 0
    j = 0
    x = (t - 1) * m + p

    while j <= x:
        string += radix(i, n, number)
        j += long(i, n)
        i += 1

    for k in range(t):
        answer += string[k * m + p - 1]

    return answer