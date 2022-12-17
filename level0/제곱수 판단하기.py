def solution(n):
    
    for i in range(1, 500001):
        if i * i == n:
            return 1
    else:
        return 2