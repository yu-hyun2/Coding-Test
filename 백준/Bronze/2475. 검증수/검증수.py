N = list(map(int, input().split()))
n=[]
for i in range(len(N)):
    n.append(N[i]**2)

print(sum(n)%10)