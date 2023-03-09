def solution(money):
    answer = [0, 0]
    i = 0
    while money >= 5500:
        money = money - 5500
        i += 1
    answer[0] = i
    answer[1] = money
    return answer