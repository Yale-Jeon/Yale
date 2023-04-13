def solution(info, query):
    answer = []
    lst = []
    for data in info:
        lst.append(data.split(' '))
    lst = sorted(lst, key = lambda x:int(x[4]), reverse=True)

    for q in query:
        x = q.split(' and ')
        y = x[-1].split(' ')
        condition = x[:-1] + y
        cnt = 0
        for applicant in lst:
            if int(applicant[-1]) < int(condition[-1]):
                break
            n = 0
            for i in range(4):
                if condition[i] == '-' or condition[i] == applicant[i]:
                    n += 1
                else:
                    break
            if n == 4:
                cnt += 1
        answer.append(cnt)

    return answer