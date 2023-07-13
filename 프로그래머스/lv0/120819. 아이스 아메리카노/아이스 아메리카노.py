def solution(money):
    answer = []
    if money < 5500:
        answer.append(0)
        answer.append(money)
    else:
        answer.append(int(money/5500)) 
        answer.append(money%5500) 
    return answer
