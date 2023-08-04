n = []
for i in range(9):
    num = int(input())
    n.append(num)

print(max(n))
print(n.index(max(n))+1)