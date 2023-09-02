a = list(int(input()) for _ in range(3))
a.remove(min(a))
a.remove(max(a))
print(*a)