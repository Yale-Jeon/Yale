def f(w1, w2):
    count = 0
    j = min(len(w1), len(w2))
    for i in range(j):
        if w1[i] == w2[i]:
            count += 1
        else:
            break
    return count


def solution(words):
    answer = 0
    words.sort()
    prev_ = -1
    next_ = -1
    for i in range(len(words)):
        if i == 0:
            prev_ = f(words[i], words[i + 1])
            answer += min(prev_ + 1, len(words[i]))
        elif i == (len(words) - 1):
            answer += min(prev_ + 1, len(words[i]))
        else:
            next_ = f(words[i], words[i + 1])
            answer += max(min(prev_ + 1, len(words[i])), min(next_ + 1, len(words[i])))
            prev_ = next_

    return answer