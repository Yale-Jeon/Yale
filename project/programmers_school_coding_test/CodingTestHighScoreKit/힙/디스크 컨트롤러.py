import heapq
def solution(jobs):
    n = len(jobs)
    answer = 0
    now = 0
    heapq.heapify(jobs)
    wait = []
    while jobs:
        while jobs:
            if jobs[0][0] <= now:
                heapq.heappush(wait, heapq.heappop(jobs)[::-1])
            else:
                break
        if len(wait) == 0:
            now = jobs[0][0]
            continue
        x = heapq.heappop(wait)
        answer += now - x[1] + x[0]
        now += x[0]

    while wait:
        x = heapq.heappop(wait)
        answer += now - x[1] + x[0]
        now += x[0]

    return int(answer/n)