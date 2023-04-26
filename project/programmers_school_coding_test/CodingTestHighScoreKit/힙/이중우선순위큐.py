import heapq
def solution(operations):
    lst = [] # list
    q = [] # heapq
    p = [] # heapq reverse
    for o in operations:
        op, num = o.split()
        if op == 'I':
            lst.append(int(num))
            heapq.heappush(q, int(num))
            heapq.heappush(p, -int(num))
        else: # op == 'D'
            if len(lst) == 0:
                continue
            if num == '1':
                x = heapq.heappop(p)
                lst.remove(-x)
                q.remove(-x)
            else: # num == '-1'
                x = heapq.heappop(q)
                lst.remove(x)
                p.remove(-x)
    if len(lst) == 0:
        return [0,0]
    return [(-1)*heapq.heappop(p), heapq.heappop(q)]