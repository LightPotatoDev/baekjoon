n = int(input())
L = list(map(int,input().split()))

streak = 0
score = 0
for i in L:
    if i == 0:
        streak = 0
    else:
        streak += 1
        score += streak
print(score)
