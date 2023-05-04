def solution(n,a,b):
    c = 1
    r = 0 # n = 2**r
    a, b = a-1, b-1
    while True: # log
        if c == n:
            break
        c *= 2
        r += 1
    for i in range(1,r+1):
        if a//2**i == b//2**i:
            answer = i
            break

    return answer