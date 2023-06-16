def solution(arr):
    i=0
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        i += 1
    answer = sum / len(arr)
        
    return answer