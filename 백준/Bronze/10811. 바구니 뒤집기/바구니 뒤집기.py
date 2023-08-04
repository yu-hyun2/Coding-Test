N, M = map(int, input().split())
bk = []
for a in range(N+1):
    bk.append(a)

for _ in range(M):
    i, j = map(int, input().split())
    
    bk[i:j+1] = bk[j:i-1:-1]
print(*bk[1:])