def solution(box, n):
    answer = 1
    for space in box:
        answer *= space // n
    return answer