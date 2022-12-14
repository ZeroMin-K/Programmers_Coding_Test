def solution(angle):
    answer = 0
    
    # 0도 초과 90도 미만 예각 - 1
    if 0 < angle < 90:
        answer = 1
    # 90도 직각 - 2
    elif angle == 90:
        answer = 2
    # 90도 초과 180도 미만 둔각 - 3
    elif 90 < angle < 180:
        answer = 3
    # 180도 평각 - 4
    else:
        answer = 4
    
    return answer