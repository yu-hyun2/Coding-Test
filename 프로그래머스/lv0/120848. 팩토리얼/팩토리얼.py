import math

def solution(n):
    i = 1
    while True:
        if math.factorial(i) > n:
            return i - 1
        i += 1