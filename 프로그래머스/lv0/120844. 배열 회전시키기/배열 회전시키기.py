def solution(numbers, direction):
    if direction == "left":
        return numbers[1:] + [numbers[0]]
    elif direction == "right":
        return [numbers[-1]] + numbers[:-1]