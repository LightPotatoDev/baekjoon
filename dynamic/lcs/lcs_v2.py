from bisect import bisect_left

s1 = input()
s2 = input()

#lcs to lis
D = dict()
L = []
for i,x in enumerate(s1):
    if x not in D:
        D[x] = [i]
    else:
        D[x] = D[x] + [i]

for i in s2:
    if i in D:
        L.append(D[i][0])
        if len(D[i]) != 1:
            D[i].pop(0)

print(L)

#solve lis
def lis(L):
    dp = [L[0]]

    for a in L[1:]:
        if a > dp[-1]:
            dp.append(a)
        else:
            index = bisect_left(dp,a)
            dp[index] = a

    return len(dp)

if len(L) == 0:
    print(0)
else:
    print(lis(L))