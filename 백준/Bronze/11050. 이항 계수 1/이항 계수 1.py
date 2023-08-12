N, K = map(int, input().split())
a=1
b=1
for i in range(N, N-K, -1):
    a*=i
for j in range(1, K):
    b*=(j+1)
print(a//b) 