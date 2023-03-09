def solution(slice, n):
    answer = 0
    if 2 <= slice <= 10:
        if 1 <= n <= 100:
            if n % slice == 0:
                answer = n // slice
            else:
                answer = (n//slice)+1
    return answer