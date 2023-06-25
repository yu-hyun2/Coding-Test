def solution(my_string):
    new_string = ""

    for char in my_string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()

    return new_string

