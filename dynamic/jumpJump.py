n = int(input())
L = list(map(int,input().split()))
dp = [int(1e9)]*n
dp[0] = 0

for i in range(n):
    if dp[i] != int(1e9):
        for j in range(1,L[i]+1):
            if i+j < n:
                dp[i+j] = min(dp[i]+1, dp[i+j])

print(dp[-1]) if dp[-1] != int(1e9) else print(-1)