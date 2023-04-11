from itertools import combinations

def is_inclusion(a,b):
    for i in a:
        if i not in b:
            return False
    return True

def solution(relation):
    answer = 0
    n = len(relation[0])
    lst = []
    comb = []
    for i in range(n): lst.append(i)
    for i in range(len(lst)): comb += list(combinations(lst, i+1))

    while True:
        if len(comb) == 0:
            break
        c = 0
        x = []
        for i in relation:
            y = []
            for j in comb[0]:
                y.append(i[j])
            if y in x:
                c = -1
                break
            else:
                x.append(y)
        if c == -1:
            comb.pop(0)
        else:
            v = comb[0]
            answer += 1
            del_list=[]
            for k in comb:
                if is_inclusion(v,k):
                    del_list.append(k)
            for d in del_list:
                comb.remove(d)

    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))