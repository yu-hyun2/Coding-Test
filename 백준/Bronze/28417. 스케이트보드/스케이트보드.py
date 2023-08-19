N = int(input())
score=[]
for i in range(N):
    li = list(map(int, input().split()))
    run = li[0:2]
    act = li[2:7]
    act = sorted(act, reverse= True)
    score.append(max(run) + act[0] + act[1])

print(max(score))
    