n = int(input())
L = []
for _ in range(n):
    L.append(int(input()))

L = L[::-1]
score = L[0]
cnt = 0
for i in L[1:]:
    if i >= score:
        cnt += i-score+1
        score -= 1
    else:
        score = i

print(cnt)
