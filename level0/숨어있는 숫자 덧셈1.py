def solution(my_string):
    
    return sum([int(i) for i in my_string if ord(i) - ord('A') < 0])