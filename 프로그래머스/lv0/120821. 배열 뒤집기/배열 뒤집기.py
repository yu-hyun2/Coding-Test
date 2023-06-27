def solution(num_list):
    answer = []

    for i in range(0, len(num_list)):

        answer.append(num_list[-(i+1)])

    return answer