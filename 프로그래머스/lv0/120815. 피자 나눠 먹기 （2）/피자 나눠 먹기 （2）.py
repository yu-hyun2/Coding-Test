def solution(n):
    answer = 1
    p = 6
    
    while p % n:
        answer += 1
        p += 6
        
    return answer