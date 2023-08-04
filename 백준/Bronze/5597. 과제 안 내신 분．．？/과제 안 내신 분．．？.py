num = [31]*(2)
for i in range(28):
    n = int(input())
    num.append(n)

num = sorted(num)

for _ in range(30):
    if _+1 not in num:
        print(_+1)