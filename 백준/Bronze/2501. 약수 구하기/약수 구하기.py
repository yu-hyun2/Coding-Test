N, K = map(int, input().split())
num = []
for i in range(N+1):
    if N % (i+1) == 0:
        num.append(i+1)

if len(num) < K:
    print(0)
else:
    print(num[K-1])