def solution(s):
    n = 0
    for x in s:
        if x == '(':
            n += 1
        else:
            n -= 1
        if n < 0: return False
    return n == 0