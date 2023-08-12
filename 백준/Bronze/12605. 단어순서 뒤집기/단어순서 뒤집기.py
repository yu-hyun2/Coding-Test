N = int(input())

for i in range(N):
    a = input().split()
    print(f'Case #{i+1}:' , *(a[::-1]))