while True:
    try:
        A, B = map(int, input().split())
        if  A == 0 & B == 0:
            break
        elif A > B:
            print('Yes')
        else:
            print('No')
    except:
        break