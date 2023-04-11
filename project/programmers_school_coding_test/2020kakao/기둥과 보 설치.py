def gd(x, y, answer):
    if y == 0:
        return True
    if ([x,y-1,0] in answer) or ([x,y,1] in answer) or ([x-1,y,1] in answer):
        return True
    return False

def bo(x, y, answer):
    if ([x,y-1,0] in answer) or ([x+1,y-1,0] in answer):
        return True
    if ([x-1,y,1] in answer) and ([x+1,y,1] in answer):
        return True
    return False

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        if build[3] == 1:
            if build[2] == 0:
                if gd(build[0], build[1], answer):
                    answer.append([build[0], build[1], 0])
            else:
                if bo(build[0], build[1], answer):
                    answer.append([build[0], build[1], 1])
        else:
            if build[2] == 0:
                while True:
                    if [build[0], build[1]+1, 0] in answer:
                        if not ([build[0], build[1]+1, 1] in answer or [build[0]-1, build[1]+1, 1] in answer):
                            break
                    if [build[0], build[1]+1, 1] in answer:
                        if not [build[0]+1, build[1], 0] in answer:
                            if not ([build[0]-1, build[1]+1, 1] in answer and [build[0]+1, build[1]+1, 1] in answer):
                                break
                    if [build[0]-1, build[1]+1, 1] in answer:
                        if not [build[0]-1, build[1], 0] in answer:
                            if not ([build[0]-2, build[1]+1, 1] in answer and [build[0], build[1]+1, 1] in answer):
                                break
                    answer.remove([build[0], build[1],0])
                    break
            else:
                while True:
                    if [build[0], build[1], 0] in answer:
                        if [build[0]-1, build[1], 1] not in answer and [build[0], build[1]-1, 0] not in answer:
                            break
                    if [build[0]+1, build[1], 0] in answer:
                        if [build[0]+1, build[1], 1] not in answer and [build[0]+1, build[1]-1, 0] not in answer:
                            break
                    if [build[0]+1, build[1], 1] in answer:
                        b = answer[::]
                        b.remove([build[0],build[1],1])
                        if not bo(build[0]+1, build[1], b):
                            break
                    if [build[0]-1, build[1], 1] in answer:
                        b = answer[::]
                        b.remove([build[0],build[1],1])
                        if not bo(build[0]-1, build[1], b):
                            break
                    answer.remove([build[0], build[1],1])
                    break
    answer = sorted(answer, key = lambda x:x[2])
    answer = sorted(answer, key = lambda x:x[1])
    answer = sorted(answer, key = lambda x:x[0])
    return answer