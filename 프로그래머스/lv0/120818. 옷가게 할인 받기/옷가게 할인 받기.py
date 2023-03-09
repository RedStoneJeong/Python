import math
def solution(price):
    answer = 0
    price = round(price, -1)
    if 10 <= price <= 1000000:
        if price < 500000:
            if price < 300000:
                if price >= 100000:
                    answer = price - (price * 0.05)
                else:
                    answer = price
            else:
                answer = price - (price * 0.1)
        else:
            answer = price - (price * 0.2)
    return math.floor(answer)