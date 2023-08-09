N = int(input())

for i in range(N):
    print('*'*(i+1) + ' '* (2*(N-i-1))+ '*'*(i+1))

for j in range(N):
    print('*'*(N-j-1) + ' '*2*(j+1) + '*'*(N-j-1))