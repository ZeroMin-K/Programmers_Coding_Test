def solution(num_list):
    odd_list = [i for i in num_list if i % 2 == 1]
    even_list = [i for i in num_list if i % 2 == 0]
    return [len(even_list), len(odd_list)]