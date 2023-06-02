T = int(input())

while T > 0:
    H, W, N = map(int, input().split(' '))

    X = (N // H) + 1
    Y = N % H
    if Y == 0:
        Y = H
        X = N // H
        
    if X < 10:
        X = '0' + str(X)
    else:
        X = str(X)
        
    room_num = int(str(Y) + X)
    print(room_num)
    T -= 1