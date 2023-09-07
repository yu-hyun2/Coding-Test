a = list(input())

if a[::1] == a[::-1]:
    answer = 1
else:
    answer = 0

print(answer)