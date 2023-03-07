def solution(array, height):
    answer = 0
    for i in array:
        if 1 <= len(array) <=100:
            if 1 <= height < i:
                answer +=1
    return answer