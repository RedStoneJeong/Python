def solution(dot):
    answer = 0
    if dot[0] * dot[1] != 0 and -250000 <= dot[0] * dot[1] <= 250000:
        if dot[0] * dot[1] >= 1:
            if dot[0] < 0:
                answer = 3
            else:
                answer = 1 
        elif dot[0] * dot[1] < 0:
            if dot[0] < 0:
                answer = 2
            else:
                answer = 4
    return answer