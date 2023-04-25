def solution(priorities, location):
    answer = 0
    n = len(priorities)
    num = priorities[location]
    max_num = sorted(list(set(priorities)), reverse=True)
    m = 0
    while True:
        lst = []
        for i, x in enumerate(priorities):
            if x == max_num[m]:
                lst.append(i)
        if max_num[m] == num:
            c = 1
            for l in lst:
                if l != location:
                    c += 1
                else:
                    break
            answer += c
            break
        else:
            answer += priorities.count(max_num[m])
            priorities = priorities[lst[-1]:] + priorities[:lst[-1]]
            if location > lst[-1]:
                location -= lst[-1]
            else:
                location += (n - lst[-1])
        m += 1

    return answer