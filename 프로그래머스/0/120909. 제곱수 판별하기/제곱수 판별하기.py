def solution(n):
    num = n ** (1/2)

    if num % 1 == 0:
        answer = 1
    else:
        answer = 2

    return answer