H, M = map(int, input().split())

H += (M-45)//60
H %= 24
M = (M-45)%60

print(H, M)