N = int(input())
a = list(map(int, input().split()))

y = []
m = []

for i in range(len(a)):
    y.append(10 + 10 * (a[i]//30))
    m.append(15 + 15 * (a[i]//60))

if sum(y) > sum(m):
    print('M', sum(m))
elif sum(y) < sum(m):
    print('Y', sum(y))
else:
    print('Y', 'M', sum(m))