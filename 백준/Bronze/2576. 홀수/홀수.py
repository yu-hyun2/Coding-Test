sum = 0
arr = []
for i in range(7):
    N = int(input())

    if N % 2 != 0:
        arr.append(N)
        sum += N
if sum == 0:
    print(-1)
else:
    print(sum)
    print(sorted(arr)[0])