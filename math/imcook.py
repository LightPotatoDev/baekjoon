winner = 0
score = 0
for i in range(5):
    s = sum(list(map(int,input().split())))
    if s > score:
        winner = i
        score = s
print(winner+1, score)