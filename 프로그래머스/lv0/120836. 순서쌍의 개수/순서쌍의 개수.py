n = 20
(1, 2, 4, 5, 10, 20)

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n/i == int(n/i):
            answer += 1
        else:
            continue
    return answer