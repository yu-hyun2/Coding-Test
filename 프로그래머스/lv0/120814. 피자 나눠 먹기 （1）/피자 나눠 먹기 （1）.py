def solution(n):
    
    if n % 7 == 0:
        answer = int(n/7)
    elif n/7 == int(n/7):
        answer = n
    else:
        answer = int(n/7)+1

    return answer