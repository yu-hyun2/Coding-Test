N = int(input())
sum = 0
while N % 4 == 0:
    sum += (N//4)
    break
print('long '*sum + 'int') 