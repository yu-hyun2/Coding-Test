a = int(input())
b = int(input())

print(a * (b-(b//10)*10))
print(a * ((b-(b//100)*100)//10))
print(a * (b//100))
print(a*b)