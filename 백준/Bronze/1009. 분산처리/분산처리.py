T = int(input())
f = []
for i in range(T):
    a, b = map(int, input().split())

    if a%10 == 0: 
        print(10)
    else:
        for j in range(1,5):
            f.append(str((a**j)%10))
        print(f[b%4-1])
        f=[]
