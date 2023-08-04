num =[0] * 31

for i in range(28):
    n = int(input())
    num[n] = n

for _ in range(1,31):
    if num[_] == 0:
        print(_)
