def solution(brown, yellow):
    x = (brown-4)/4
    y = ((((brown-4)/2)**2-4*yellow)**0.5)/2
    return [int(x+y+2),int(x-y+2)]