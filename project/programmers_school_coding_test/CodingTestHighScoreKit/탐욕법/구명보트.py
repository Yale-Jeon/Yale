def solution(people, limit):
    n = len(people)
    if n == 1:
        return 1
    answer = 0
    people.sort(reverse=True)
    start = 0
    end = n-1
    while True:
        if start > end:
            break
        c = people[start]
        while True:
            if start < end and c + people[end] <= limit:
                end -= 1
                c += people[end]
            else:
                break
        answer += 1
        start += 1
    return answer