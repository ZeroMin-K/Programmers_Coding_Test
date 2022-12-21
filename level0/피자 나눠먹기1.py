def solution(n):
    d, m = divmod(n, 7)
    return d + int(m != 0)