from itertools import permutations
def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    lst = list(numbers)
    result = []
    for i in range(1,len(lst)+1):
        for x in permutations(lst, i):
            if is_prime(int(''.join(x))):
                result.append(int(''.join(x)))
    return len(set(result))