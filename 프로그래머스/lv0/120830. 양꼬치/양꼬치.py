def solution(n, k):
    a = 12000
    b = 2000
    m = int(n/10)
    if m >= 1:
        answer = n*a + k*b - 2000*m
    else:
        answer = n*a + k*b
    return answer