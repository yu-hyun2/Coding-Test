N, M = map(int, input().split(' '))

cards = list(map(int, input().split(' ')))[:N]

result = []
fst_card = cards.copy()
for i in cards:
    fst_card.remove(i)
    scnd_card = fst_card.copy()
    for j in fst_card:
        scnd_card.remove(j)
        for k in scnd_card:
            cards_sum = i + j + k
            if cards_sum <= M:
                result.append(cards_sum)
                
print(max(result))