n = int(input())
L = list(map(int,input().split()))
dp = [[0]*n for _ in range(2)]
dp[0][0] = max(0,L[0])

for i in range(1,n):
    dp[0][i] = max(0,dp[0][i-1] + L[i])

for i in range(1,n):
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + L[i])

for r in dp:
    print(r)
ans = max([max(dp[i]) for i in range(2)])
print(ans if ans != 0 else max(L))