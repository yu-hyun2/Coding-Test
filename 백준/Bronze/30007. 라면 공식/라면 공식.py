N = int(input())

for i in range(N):
    a = list(map(int, input().split()))
    print(a[0] * (a[2] - 1) + a[1])