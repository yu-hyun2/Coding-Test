N = list(input())
a = ['a', 'e', 'i', 'o', 'u']
sum = 0
for i in N:
    if i in a:
        sum += 1
print(sum)