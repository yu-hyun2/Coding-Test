N = int(input())
a = list(map(int, input().split()))

for i in a:
    if i < i+1:
        a

print(min(a), max(a))