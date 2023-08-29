n,s,m = map(int,input().split())
V = list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(2)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[0][j] == 1:
            if 0 <= j-V[i] <= m:
                dp[1][j-V[i]] = 1
            if 0 <= j+V[i] <= m:
                dp[1][j+V[i]] = 1

    dp[0] = dp[1][:]
    dp[1] = [0]*(m+1)

try:
    print(m-dp[0][::-1].index(1))
except:
    print(-1)


