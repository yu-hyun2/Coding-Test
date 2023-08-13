a = list(input())

for i in range(len(a)):
    if a[i].isupper() == True:
        print(a[i].lower(), end='')
    else:
        print(a[i].upper(), end='')