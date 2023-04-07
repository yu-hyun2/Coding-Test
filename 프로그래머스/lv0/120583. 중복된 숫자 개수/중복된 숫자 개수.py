from collections import Counter

def solution(array, n):
    return Counter(array).get(n)