def solution(n, times):
    x = 0
    y = 10 ** 18
    i = 0
    while i < 100:
        mid = int((x + y) / 2)
        c = 0
        is_over = False
        if x == y:
            break
        for t in times:
            c += int(mid / t)
            if c >= n:
                is_over = True
                break
        if is_over:
            y = mid
        else:
            x = mid + 1
        i += 1
    return x