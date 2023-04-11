def check(word, a, b):
    n = len(a)
    if b == 1:  # b=1 앞에서부터, b=0 뒤에서부터
        for i in range(n):
            if word[i] != a[i]:
                return False
    else:
        for i in range(n):
            if word[-(i + 1)] != a[-(i + 1)]:
                return False
    return True


def solution(words, queries):
    n = len(queries)
    answer = [0] * n
    d = {}  # d[5] = [['fro', 1, 0],['o', 0, 1]]
    for i in range(n):
        k = len(queries[i])
        if queries[i][0] == '?':
            if k in d:
                d[k].append([queries[i][queries[i].count('?'):], 0, i])
            else:
                d[k] = [[queries[i][queries[i].count('?'):], 0, i]]
        else:
            if k in d:
                d[k].append([queries[i][:(-1) * queries[i].count('?')], 1, i])
            else:
                d[k] = [[queries[i][:(-1) * queries[i].count('?')], 1, i]]

    for word in words:
        m = len(word)
        if m not in d:
            continue
        for keyword in d[m]:
            if check(word, keyword[0], keyword[1]):
                answer[keyword[2]] += 1
    return answer