import re

def solution(files):
    answer = []
    lst =[]
    for i in range(len(files)):
        file = files[i]
        head = re.split('\d+', file)[0].lower()
        number = int(re.findall('\d+', file)[0])
        lst.append([head,number,i])
    lst = sorted(lst, key=lambda x:x[1])
    lst = sorted(lst, key=lambda x:x[0])
    for f in lst:
        answer.append(files[f[2]])
    return answer