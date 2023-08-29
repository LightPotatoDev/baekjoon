n,l,k = map(int,input().split())
sub1 = []
sub2 = []
for _ in range(n):
    s1,s2 = map(int,input().split())
    sub1.append(s1)
    sub2.append(s2)

score = 0

for i,x in enumerate(sub2):
    if k == 0:
        break
    if x <= l:
        score += 140
        sub1[i] = 999
        k -= 1

for i in sub1:
    if k == 0:
        break
    if i <= l:
        score += 100
        k -= 1

print(score)