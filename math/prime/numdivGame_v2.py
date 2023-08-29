n = int(input())
L = list(map(int,input().split()))
cards = [0]*1000001
for i in L:
    cards[i] = 1

score = [0]*1000001
for i in L:
    for j in range(i*2, 1000001, i):
        if cards[j] == 1:
            score[i] += 1
            score[j] -= 1

for i in L:
    print(score[i], end = ' ')