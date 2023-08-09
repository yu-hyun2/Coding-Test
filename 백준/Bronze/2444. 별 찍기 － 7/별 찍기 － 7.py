N = int(input())

for i in range(N):
    print(' '*(N-i-1) + '*'*(2*(i+1)-1))

for j in range(N):
    print(' '*(j+1) + '*'*(2*(N-j-1)-1))