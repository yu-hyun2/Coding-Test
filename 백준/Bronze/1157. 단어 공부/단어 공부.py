a = list(input().upper())
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
answer = []
cnt = []
for j in range(len(b)):
    cnt.append(a.count(b[j]))

for _ in range(len(b)):
    if a.count(b[_]) == max(cnt):
        answer.append(b[_])

if len(answer) >= 2:
    print('?')
else:
    print(*answer)