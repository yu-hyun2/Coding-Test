def solution(x, n):
    i = 0
    sum =0
    answer = []
    
    for i in range(n):
        sum += x
        answer.append(sum)
        i +=1
    
    return answer