N = int(input())
sum = 0
for i in range(N):
    sum += 1
    print(f'{" "*(N-sum)}'+'*'*sum)