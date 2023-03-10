def solution(array):
    answer = 0
    array = sorted(array)
    if len(array) % 2 == 1:
        if 0 < len(array) < 100:
            for i in array:
                if -1000 < i < 1000:
                    answer = array[len(array)//2]                      
    return answer