def solution(word):
    dic = {'A':0,'E':1,'I':2,'O':3,'U':4}
    di = [781,156,31,6,1]
    answer = 0
    for i, w in enumerate(word):
        answer += di[i]*dic[w]+1
    return answer