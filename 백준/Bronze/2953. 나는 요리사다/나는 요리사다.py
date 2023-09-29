a = []

for i in range(5):
    n =  list(map(int, input().split()))
    a.append(sum(n))

for i in range(5):
    if a[i] == max(a):
        print(i+1, a[i])