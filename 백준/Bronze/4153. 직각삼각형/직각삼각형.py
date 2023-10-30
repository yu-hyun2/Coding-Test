# BOJ 4153

a, b, c = map(int, input().split())

while (a != 0) & (b != 0) & (c != 0):
    if (a**2 + b**2 == c**2) | (a**2 + c**2 == b**2) | (b**2 + c**2 == a**2):
        print('right')
    else:
        print('wrong')
    a, b, c = map(int, input().split())