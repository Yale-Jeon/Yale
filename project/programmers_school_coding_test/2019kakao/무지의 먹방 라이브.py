def solution(food_times, k):
    answer = 0
    food_sum = sum(food_times)
    if k >= food_sum:
        answer = -1
    else:
        food =[]
        for i in range(len(food_times)):
            food.append([food_times[i], i+1])
        food = sorted(food, key = lambda x:x[0])
        n = len(food)
        c=0
        last=0
        for j in range(n):
            if k > (food[j][0]-last)*(n-j):
                k -= (food[j][0]-last)*(n-j)
                last = food[j][0]
            else:
                c=j
                break
        food2 = []
        for j in range(n-c):
            food2.append(food[j+c])
        food2 = sorted(food2, key = lambda x:x[1])
        answer = food2[(k)%(n-c)][1]
    return answer