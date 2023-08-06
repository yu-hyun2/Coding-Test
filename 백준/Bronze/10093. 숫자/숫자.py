num = []
sum = 0
A, B = map(int, input().split())

if A < B:
    for i in range(A+1,B):
        sum += 1
        num.append(i)

else:
    for i in range(B+1,A):
        sum += 1
        num.append(i)

print(sum)
print(*num)