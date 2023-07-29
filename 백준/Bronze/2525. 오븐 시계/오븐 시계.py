A, B = map(int, input().split())
C = int(input())

if B + C >= 60:
    A += (B+C) // 60
    A %= 24
    B = (B+C) % 60
else:
    B += C

print(A, B)