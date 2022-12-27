def solution(sides):
    # 삼각형 변 정렬
    sides.sort()
    
    return 1 if sides[2] < sides[0] + sides[1] else 2