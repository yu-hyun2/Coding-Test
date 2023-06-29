def solution(arr):

    answer = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            answer.append(arr[i])
        else:
            continue

    return answer