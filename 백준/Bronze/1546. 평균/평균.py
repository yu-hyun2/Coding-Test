N = int(input())

m = list(map(int, input().split()))
M = max(m)

for i in range(len(m)):
    m[i] = m[i]/M*100

print(sum(m)/len(m))