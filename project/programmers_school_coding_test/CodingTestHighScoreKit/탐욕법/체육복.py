def solution(n, lost, reserve):
    intersection = set(lost).intersection(set(reserve))
    lost = list(set(lost).difference(intersection))
    reserve = list(set(reserve).difference(intersection))
    lost.sort()
    reserve.sort()
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    return n-len(lost)