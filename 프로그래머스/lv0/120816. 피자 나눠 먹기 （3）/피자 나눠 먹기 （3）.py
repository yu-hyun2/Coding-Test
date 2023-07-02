def solution(slice, n):
    answer = 0
    if n <= slice:
        answer = 1
    elif n/slice == int(n/slice):
        answer = int(n/slice)
    else:
        answer = int(n/slice)+1
    
    return answer