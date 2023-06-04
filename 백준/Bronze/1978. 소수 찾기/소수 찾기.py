n = int(input())

nums = list(map(int, input().split(' ')))

answer = []
for i in nums:
    result = []
    for j in range(1, i+1):
        if i % j == 0:
            result.append(j)
    if len(result) == 2:
        answer.append(i)
        
print(len(answer))