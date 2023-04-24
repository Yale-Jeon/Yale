from collections import defaultdict
def solution(genres, plays):
    if len(plays) == 1:
        return[0]
    n = len(genres)
    d = defaultdict(lambda: 0)
    d_lst = defaultdict(lambda: [])
    answer = []
    for i in range(n):
        d[genres[i]] += plays[i]
        if len(d_lst[genres[i]]) == 0:
            d_lst[genres[i]].append(i)
        elif len(d_lst[genres[i]]) == 1:
            if plays[d_lst[genres[i]][0]] < plays[i]:
                d_lst[genres[i]].insert(0, i)
            else:
                d_lst[genres[i]].append(i)
        else:
            if plays[d_lst[genres[i]][0]] < plays[i]:
                d_lst[genres[i]].insert(0, i)
            else:
                if plays[d_lst[genres[i]][1]] < plays[i]:
                    d_lst[genres[i]].insert(1, i)                        

    l = sorted(list(d.items()), key=lambda x:x[1], reverse=True)
    for x in l:
        answer += d_lst[x[0]][:2]

    return answer