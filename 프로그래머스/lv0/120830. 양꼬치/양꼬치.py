def solution(n, k):
    answer = 0
    if n >= 10:
        if n < 20:
            answer = n*12000 + (k-1)*2000
        elif n >= 20:
            answer = n*12000 + (k-(n//10))*2000
    else:
         answer = n*12000 + k*2000   
    return answer