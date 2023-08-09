N = int(input())

for i in range(N): 
    print(' '*i + '*'*(2*(N-i)-1))

for j in range(N-1):
    print(' '*((N-j-1)-1) + '*'*(2*(j+1)+1))