def solution(number, k):
    n = len(number)
    result = ''
    lst = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    start = 0
    for j in range(n - k):
        for i in range(10):
            index = number[start:k + j + 1].find(lst[i])
            if index != -1:
                break
        result += number[index + start]
        start = index + start + 1
    return result