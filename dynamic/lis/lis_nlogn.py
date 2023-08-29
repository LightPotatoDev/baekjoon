import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
dp = [L[0]]

save = [L[0]]
best = False

for a in L[1:]:
    if a > dp[-1]:
        dp.append(a)
        if best == False:
            save = dp[:]
            best = True
        else:
            save.append(a)
    else:
        index = bisect_left(dp,a)
        dp[index] = a
        best = False

print(len(dp))
print(*save)