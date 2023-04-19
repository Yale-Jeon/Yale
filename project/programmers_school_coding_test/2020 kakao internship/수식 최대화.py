import re
from itertools import permutations

def calc(n1, n2, a):
    if a == '+':
        return n1 + n2
    elif a == '-':
        return n1 - n2
    else:
        return n1 * n2

def solution(expression):
    result = []
    numbers = re.findall('\d+', expression)
    numbers = list(map(int, numbers))
    a = re.findall('[*+-]', expression)
    c = ''
    if '*' in a and '*' not in c: c += '*'
    if '+' in a and '+' not in c: c += '+'
    if '-' in a and '-' not in c: c += '-'
    lst = list(permutations(c, len(c)))
    for i in lst:
        x = a[::]
        y = numbers[::]
        for j in i:
            n = 0
            while n < len(x):
                if j != x[n]:
                    n += 1
                    continue
                else:
                    aa = x.pop(n)
                    n1 = y.pop(n)
                    n2 = y.pop(n)
                    y.insert(n, calc(n1, n2, aa))
        result.append(abs(y[0]))

    answer = max(result)
    return answer