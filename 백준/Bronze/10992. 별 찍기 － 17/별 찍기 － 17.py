N = int(input())

for i in range(N-1):
    if i == 0:
        print(' '*(N-i-1) + '*')
    else:
        print(' '*(N-i-1) + '*' + ' '*(2*i-1) + '*')
print('*'*(2*N-1))