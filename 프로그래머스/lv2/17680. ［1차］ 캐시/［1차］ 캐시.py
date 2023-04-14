from collections import deque

def solution(cacheSize, cities):
    l = [''] * cacheSize
    cache = deque(l, maxlen=cacheSize)
    answer = 0 # 시간
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5 

    return answer