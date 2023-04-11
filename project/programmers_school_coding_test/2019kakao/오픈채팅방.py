def solution(record):
    answer = []
    chat = []
    dict_id = {}
    for i in record:
        a = i.split()
        if a[0] == 'Enter':
            chat.append([a[0], a[1]])
            dict_id[a[1]] = a[2]
        elif a[0] == 'Leave':
            chat.append([a[0], a[1]])
        else:
            dict_id[a[1]] = a[2]

    for j in chat:
        if j[0] == 'Enter':
            answer.append(dict_id[j[1]] + "님이 들어왔습니다.")
        elif j[0] == 'Leave':
            answer.append(dict_id[j[1]] + "님이 나갔습니다.")

    return answer