def solution(array):
    array.sort()
    num = int(len(array)/2)
    answer = array[num]
    return answer
