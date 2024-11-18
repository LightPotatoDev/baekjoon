import sys
input = sys.stdin.readline

c,n = map(int,input().split())
info = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(c+1) for _ in range(n+1)]

def get_dp_value(i,j,cost,ppl):
    res = 0
    for k in range(1,j//cost+1):
        res = max(res, dp[i-1][j-k*cost] + k*ppl)
    return res

for i in range(1,n+1):
    cost, ppl = info[i-1]
    for j in range(1,c+1):
        dp[i][j] = max(dp[i][j-1], get_dp_value(i,j,cost,ppl))

for row in dp:
    print(row)