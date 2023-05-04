def solution(name):
    answer = 0
    dic = {'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
           'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}
    move_lst = []
    for i, n in enumerate(name):
        if n != 'A':
            answer += dic[n]
            if i != 0:
                move_lst.append(i)
    if len(move_lst) == 0: return answer

    result = [len(name) - move_lst[0], move_lst[-1]]
    if len(move_lst) >= 2:
        for i in range(len(move_lst) - 1):
            result.append(move_lst[i] * 2 + len(name) - move_lst[i + 1])
            result.append(move_lst[i] + (len(name) - move_lst[i + 1]) * 2)

    return answer + min(result)