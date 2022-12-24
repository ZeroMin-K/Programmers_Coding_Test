def solution(my_string, n):
    answer = []
    for word in my_string:
        answer.append(word * n)
    return ''.join(answer)