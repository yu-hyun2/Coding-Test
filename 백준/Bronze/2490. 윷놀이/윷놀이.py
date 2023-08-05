u = ['A', 'B', 'C', 'D', 'E']


for i in range(3):
    a = list(map(int, input().split()))
    count = 0
    for j in range(4):
        if a[j] == 0:
            count += 1
    print(u[count-1])