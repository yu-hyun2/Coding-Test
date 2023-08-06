num = []
sum = 0

for i in range(5):
    n = int(input())
    num.append(n)
    sum += n

print(sum//5)
print(sorted(num)[2])