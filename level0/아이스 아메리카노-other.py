def solution(money):
    cups = money // 5500
    rest = money % 5500
    
    return [cups, rest]