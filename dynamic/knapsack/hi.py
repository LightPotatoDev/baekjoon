n = int(input())
health = [0]+list(map(int,input().split()))
pleasure = [0]+list(map(int,input().split()))

dp = [[0]*(100) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,100):
        if j < health[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-health[i]]+pleasure[i])

print(dp[n][99])
for row in dp:
    print(row)