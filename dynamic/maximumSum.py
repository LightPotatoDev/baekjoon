import sys
input = sys.stdin.readline

SIZE = 1000
n = int(input())
dp = [[0]*(SIZE+1) for _ in range(n)]
recent = [-1]*(SIZE+1)

def find_maxsum(i,x):
    val = 0
    for j in range(1,x+1):
        if recent[j] == -1:
            continue
        val = max(val,dp[recent[j]][j])
    return val

for i in range(n):
    L = set(map(int,input().split()[1:]))
    for x in L:
        if i == 0:
            dp[0][x] = x
        elif i != 0:
            dp[i][x] = find_maxsum(i,x) + x
    for x in L:
        recent[x] = i

ans = 0
for i in range(n):
    for j in range(SIZE+1):
        ans = max(dp[i][j],ans)
print(ans)