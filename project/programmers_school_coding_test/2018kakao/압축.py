def solution(msg):
    answer = []
    d = {}
    d_max = 27
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(msg)
    for i in range(26):
        d[alphabet[i]] = i + 1
    j = 0
    while j < len(msg):
        if j == len(msg) - 1:
            answer.append(d[msg[j]])
            break
        s = msg[j]
        while True:
            if s in d:
                if j == len(msg) - 1:
                    answer.append(d[s])
                    j += 1
                    break
                else:
                    j += 1
                    s += msg[j]
            else:
                d[s] = d_max
                d_max += 1
                answer.append(d[s[:-1]])
                break

    return answer