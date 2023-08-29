l = [['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O'], ['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z']]
a = list(input())
sum = 0

for i in range(len(a)):
    for j in range(len(l)):
        if a[i] in l[j]:
            sum += j+3
print(sum)