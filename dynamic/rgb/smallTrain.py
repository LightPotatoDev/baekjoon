n = int(input())
L = list(map(int,input().split()))
m = int(input())

prefix = [0,L[0]]
for i in range(1,n):
    prefix.append(prefix[-1] + L[i])

m_prefix = [prefix[i+m]-prefix[i] for i in range(n-m+1)]
dp = [[0]*(n-m+1) for _ in range(3)]
for i in range(3):
    for j in range(n-m+1):
        if i != 0 and j >= m:
            dp[i][j] = max(dp[i-1][j-m], dp[i][j-1])
    for j in range(n-m+1):
        dp[i][j] += m_prefix[j]

print(max(dp[2]))