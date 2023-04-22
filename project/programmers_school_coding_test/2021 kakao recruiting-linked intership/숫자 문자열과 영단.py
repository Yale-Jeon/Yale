import re
def solution(s):
    answer = 0
    lst1=['zero','one','two','three','four','five','six','seven','eight','nine']
    lst2=[0,1,2,3,4,5,6,7,8,9]
    for i in range(10):
        s = re.sub(lst1[i],str(lst2[i]),s)
    answer=int(s)
    return answer