N = int(input())

for i in range(N):
    
    if i == 0:
        print(' '*(N-i-1)+'*')
    else:
        print(' '*(N-i-1) + '*' + ' '*(i-1) + ' '*(i) + '*')