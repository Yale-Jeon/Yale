def solution(n, times):
    m = len(times)
    times.sort()
    wait = times[::]
    for i in range(n): #손님 당
        for j in range(m): #심사관 당
            if j == m-1:
                last = wait[j]
                wait[j] += times[j]
                break
            if wait[j] < wait[j+1]:
                last = wait[j]
                wait[j] += times[j]
                break
    answer = last
    return answer

def solution(n, times):
    times.sort()
    wait = times[::]
    for i in range(n):
        x = min(wait)
        index = wait.index(x)
        wait[index] += times[index]
    answer = x
    return answer

import heapq
def solution(n, times):
    wait = []
    for t in times:
        heapq.heappush(wait, (t,t))
    #wait = [(t,t) for t in times]
    #heapq.heapify(times)

    for i in range(n):
        x = heapq.heappop(wait)
        heapq.heappush(wait, (x[0]+x[1],x[1]))
        last = x[0]

    return last

# 모두 시간 초과
