N, X = map(int, input().split())
A = list(map(int, input().split()))
a = []

for i in A:
    if i < X:
        print(i, end=' ')