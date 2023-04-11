def solution(str1, str2):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    str1 = str1.lower()
    str2 = str2.lower()
    union1={}
    union2={}
    for i in range(len(str1)-1):
        if (str1[i] in alphabet) and (str1[i+1] in alphabet):
            x = str1[i]+str1[i+1]
            if x in union1:
                union1[x] += 1
            else:
                union1[x] = 1
    for i in range(len(str2)-1):
        if (str2[i] in alphabet) and (str2[i+1] in alphabet):
            x = str2[i]+str2[i+1]
            if x in union2:
                union2[x] += 1
            else:
                union2[x] = 1
    A = union1.keys()
    B = union2.keys()
    keys = []
    J1=0
    J2=0
    for a in A:
        if a not in keys:
            keys.append(a)
    for b in B:
        if b not in keys:
            keys.append(b)
    for key in keys:
        if key in union1:
            if key in union2:
                J1 += min(union1[key], union2[key])
                J2 += max(union1[key], union2[key])
            else:
                J2 += union1[key]
        else:
            if key in union2:
                J2 += union2[key]
    if J2==0:
        return 65536
    answer = int((J1/J2)*65536)
    return answer