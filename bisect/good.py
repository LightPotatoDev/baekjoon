from collections import defaultdict

n = int(input())
L = list(map(int,input().split()))
L.sort()
D = defaultdict(int)

for i in L:
    D[i] += 1

ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        targ = L[i] - L[j]
        good = False

        if (targ in D):
            D[targ] -= 1
            if targ != L[i] and targ != L[j]:
                ans += 1
                good = True
            elif (targ == L[i] or targ == L[j]) and D[targ] >= 2:
                ans += 1
                good = True
            D[targ] += 1

        if good:
            break
print(ans)