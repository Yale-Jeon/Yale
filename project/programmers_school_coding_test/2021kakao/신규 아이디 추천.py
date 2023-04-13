import re

def solution(new_id):
    new_id = new_id.lower()
    a = re.findall('[a-z0-9-_.]+', new_id)
    ret = ''
    for s in a:
        ret += s
    b = ret.split('.')
    ret = ''
    for s in b:
        if s != '':
            if ret == '':
                ret = s
            else:
                ret += '.'
                ret += s
    if ret == '':
        ret = 'a'
    if len(ret) > 15:
        ret = ret[:15]
    while True:
        if ret[-1] == '.':
            ret = ret[:(len(ret)-1)]
        else:
            break
    while True:
        if len(ret)<3:
            ret += ret[-1]
        else:
            break
    answer = ret
    return answer