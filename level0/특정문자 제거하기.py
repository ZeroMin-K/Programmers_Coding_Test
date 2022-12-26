def solution(my_string, letter):
    my_string = list(my_string)
    answer = [word for word in my_string if word not in letter]
    return ''.join(answer)