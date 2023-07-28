H, M = map(int, input().split())
if M == 45:
    M = 00
elif (M - 45) % 60 == 0:
    H += ((M-45) // 60)
    M = 15
elif (M - 45) < 0:
    H += ((M-45) // 60)
    if H < 0:
        H += 24
    M = 60 - 45 + M
elif (M - 45) > 0:
    H += ((M-45) // 60)
    M -= 45

print(H, M)