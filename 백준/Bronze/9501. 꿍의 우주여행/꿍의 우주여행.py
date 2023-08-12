T = int(input())

for i in range(T):
    N, D = map(int, input().split())
    sum = 0

    for j in range(N):
        v, f, c = map(int, input().split())
        if D/v <= f/c:
            sum +=1
    print(sum)
