# 효율성 테스트 탈락
def solution(sticker):
    answer = []
    q = []  # (score, i)
    n = len(sticker)
    if n <= 2:
        return max(sticker)
    sticker2 = sticker[::]
    sticker.pop(-1)  # 0번을 골랐을 때
    n -= 1
    d = {}
    for i in range(n):
        d[i] = 1
    q.append(((-1) * sticker[0], 2))
    while q:
        s, i = q.pop(0)
        if i > n - 1:
            answer.append(s)
            continue
        elif i == n - 1:
            answer.append(s - sticker[i])
            continue
        if d[i] > s:
            d[i] = s
            q.append((s - sticker[i], i + 2))
            q.append((s, i + 1))

    d = {}
    q = []
    n += 1
    for i in range(n):
        d[i] = 1
    q.append((0, 1))
    while q:
        s, i = q.pop(0)
        if i > n - 1:
            answer.append(s)
            continue
        elif i == n - 1:
            answer.append(s - sticker2[i])
            continue
        if d[i] > s:
            d[i] = s
            q.append((s - sticker2[i], i + 2))
            q.append((s, i + 1))

    return min(answer) * (-1)

# dynamic programming 효율성 더 떨어짐
def dp(score, lst):
    if len(lst) == 0:
        return score
    if len(lst) <= 2:
        return score + max(lst)
    return max(dp(score+lst[0],lst[2:]), dp(score+lst[1],lst[3:]))
def solution(sticker):
    return max(dp(sticker[0], sticker[2:-1]), dp(0, sticker[1:]))


# 효율성 부문 탈락2
import heapq
def solution(sticker):
    answer = 0
    q = []  # (score, i)
    n = len(sticker)
    if n <= 2:
        return max(sticker)
    n -= 1
    d = {}
    for i in range(n):
        d[i] = 1
    heapq.heappush(q, ((-1) * sticker[0], sticker[2:-1], 2))

    while q:
        score, lst, i = heapq.heappop(q)
        if len(lst) == 0:
            answer = min(answer, score)
            continue
        if len(lst) <= 2:
            answer = min(answer, score - max(lst))
            continue
        if d[i] <= score:
            continue
        d[i] = score
        heapq.heappush(q, (score - lst[0], lst[2:], i + 2))
        heapq.heappush(q, (score - lst[1], lst[3:], i + 3))

    d = {}
    n += 1
    for i in range(n):
        d[i] = 1
    heapq.heappush(q, (0, sticker[1:], 1))

    while q:
        score, lst, i = heapq.heappop(q)
        if len(lst) == 0:
            answer = min(answer, score)
            continue
        if len(lst) <= 2:
            answer = min(answer, score - max(lst))
            continue
        if d[i] <= score:
            continue
        d[i] = score
        heapq.heappush(q, (score - lst[0], lst[2:], i + 2))
        heapq.heappush(q, (score - lst[1], lst[3:], i + 3))

    return answer * (-1)