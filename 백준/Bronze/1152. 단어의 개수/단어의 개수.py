s = input()
str = s.split()
cnt = 0
for i in str:
    if i != '':
        cnt += 1

print(cnt)