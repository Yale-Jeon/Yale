import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        if a >= K:
            break
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+2*b)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer