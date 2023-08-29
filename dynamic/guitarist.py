n,s,m = map(int,input().split())
V = list(map(int,input().split()))

dp = [[] for _ in range(2)]
dp[0].append(s)

for i in range(n):
    volumes = [j+V[i] for j in dp[0]] + [j-V[i] for j in dp[0]]
    for v in volumes:
        if 0 <= v <= m:
            dp[1].append(v)
    dp[0] = dp[1][:]
    dp[1] = []

print(max(dp[0], default=-1))


