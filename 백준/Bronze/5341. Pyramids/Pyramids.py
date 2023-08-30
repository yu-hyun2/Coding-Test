
n = int(input())

while n != 0:
    sum = 0
    for i in range(n):
        sum += (n-i)
        
    print(sum)
    n = int(input())