def solution(n, arr1, arr2):
    result = []
    for i, j in zip(arr1, arr2):
        result.append(bin(i | j)[2:].zfill(n).replace('0', ' ').replace('1', '#'))
    return result