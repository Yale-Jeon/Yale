def solution(numbers):
    lst = list(map(str, numbers))
    x = sorted(lst, reverse=True)
    for i in range(1, len(x)):
        for j in range(i):
            if int(x[i - 1 - j] + x[i - j]) < int(x[i - j] + x[i - 1 - j]):
                x[i - 1 - j], x[i - j] = x[i - j], x[i - 1 - j]
            else:
                break
    return ''.join(x)

from itertools import permutations
def solution(numbers):
    answer=''
    d = {}
    for i in range(10):
        d[str(i)] = []
    for n in numbers:
        d[str(n)[0]].append(str(n))

    for i in range(10):
        if d[str(9-i)] == []:
            continue
        elif len(d[str(9-i)]) == 1:
            answer += d[str(9-i)][0]
        else:
            lst = []
            for s in list(permutations(d[str(9-i)], len(d[str(9-i)]))):
                lst.append(int(''.join(s)))
            answer += str(max(lst))
    return answer

from itertools import permutations


def comparision(x, y):
    if int(x + y) > int(y + x):
        return True
    else:
        return False


def solution(numbers):
    if len(numbers) == 1:
        return str(numbers[0])
    answer = [str(numbers.pop(0))]
    for n in numbers:
        answer.append(str(n))
        for i in range(len(answer) - 1):
            if comparision(answer[-1 - i], answer[-2 - i]):
                answer[-1 - i], answer[-2 - i] = answer[-2 - i], answer[-1 - i]
            else:
                break

    return ''.join(answer)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    answer = ''.join(numbers)
    if answer[0] == '0':
        return '0'
    return answer