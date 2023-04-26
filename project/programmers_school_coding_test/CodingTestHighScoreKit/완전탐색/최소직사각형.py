def solution(sizes):
    max_num = 0
    min_num = 0
    for size in sizes:
        if max(size) > max_num:
            max_num = max(size)
        if min(size) > min_num:
            min_num = min(size)
    return max_num * min_num