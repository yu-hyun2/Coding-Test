def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
      try:
        answer += int(my_string[i])
      except:
        ValueError

    return answer