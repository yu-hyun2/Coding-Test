def solution(array):
    frequency = {}
    for num in array:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    max_count = 0
    modes = []
    for num, count in frequency.items():
        if count > max_count:
            max_count = count
            modes = [num]
        elif count == max_count:
            modes.append(num)
    
    if len(modes) > 1:
        return -1
    else:
        return modes[0]