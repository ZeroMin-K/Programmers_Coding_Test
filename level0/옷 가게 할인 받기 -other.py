def solution(price):
    discount_rate = {500000:0.8, 300000:0.9, 100000: 0.95, 0:1}
    for standard, rate in discount_rate.items():
        if price >= standard:
            return int(price * rate)