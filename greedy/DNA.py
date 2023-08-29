n,m = map(int,input().split())
S = []
for _ in range(n):
    S.append(input())

ans = []
dist = 0
for i in range(m):
    D = {"A":0, "C":0, "G":0, "T":0}
    for s in S:
        D[s[i]] += 1

    most = max(D, key = D.get)
    ans.append(most)
    dist += n-D[most]

print(''.join(ans))
print(dist)