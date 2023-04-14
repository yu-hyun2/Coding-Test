# #1
# import re

# def solution(my_string):
#     return re.sub(r'[aeiou]', '', my_string)

# #2
# def solution(my_string):
#     return my_string.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

#3 정규표현식
import re

def solution(my_string):
    return re.sub(r'[aeiou]','', my_string)