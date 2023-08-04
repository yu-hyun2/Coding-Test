N, M = map(int, input().split())

a = [0] * (N)

for _ in range(M):
    i, j, k = map(int, input().split())
    for id in range(i-1, j):
        a[id] = k
 



print(*a)
