N = int(input())
st = ['give you up', 'let you down', 'run around and desert you', 'make you cry', 'say goodbye', 'tell a lie and hurt you','stop']
answer = []

for i in range(N):
    S = input()
    if S[:12] != 'Never gonna ':
        answer = 'Yes'
        break
    else:
        if S[12:] not in st:
            answer = 'Yes'
            break
        else:
            answer = 'No'

print(answer)