def solution(my_string):
    alphas = ['a', 'e', 'i', 'o', 'u']
    for alpha in alphas:
        my_string = my_string.replace(alpha, '')
    return my_string