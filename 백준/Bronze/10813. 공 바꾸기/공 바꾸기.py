N, M = map(int, input().split())
n=[]

for id in range(N):
    n.append(id+1)

for _ in range(M):
    i, j = map(int, input().split())
    n[i-1], n[j-1] = n[j-1], n[i-1]
print(*n)