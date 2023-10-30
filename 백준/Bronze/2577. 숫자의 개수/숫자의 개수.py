A = int(input())
B = int(input())
C = int(input())


n = list(str(A * B * C))

n = list(map(int, n))

for i in range(10):
    print(n.count(i))