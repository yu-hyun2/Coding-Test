n = int(input())

if n % 2 == 0:
  answer = (1 + n) * (n // 2)
else:
  answer = (1 + n) * (n // 2) + ((n + 1) // 2)

print(answer)