def solution(my_string):
    unique_chars = set()
    result = ""

    for char in my_string:
        if char not in unique_chars:
            unique_chars.add(char)
            result += char

    return result