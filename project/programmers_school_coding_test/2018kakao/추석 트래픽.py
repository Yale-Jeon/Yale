def solution(lines):
    x_list = []
    y_list = []
    max_t = -1
    for i in lines:
        x = i.split(' ')[1].split(':')
        y = float(x[0])*3600 + float(x[1])*60 + float(x[2])
        t = float(i.split(' ')[2][:-1])
        x_list.append(round(y-t-0.999,3))
        x_list.append(round(y,3))
        y_list.append([round(y-t+0.001,3), round(y,3)])
    for time in x_list:
        t=0
        for y in y_list:
            if y[0]<=round(time+0.999,3) and time<=y[1]:
                t += 1
        if t > max_t:
            max_t = t
    answer = max_t
    return answer