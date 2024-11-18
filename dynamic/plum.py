import sys
input = sys.stdin.readline

t,w = map(int,input().split())
pos = [int(input()) for _ in range(t)]
dp = [[0]*(w+1) for _ in range(t)]

if pos[0] == 1:
    dp[0][0] = 1
else:
    dp[0][1] = 1

for i in range(1,t):
    for j in range(w+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + int(pos[i] == 1)
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + int(pos[i]%2 == (j+1)%2)

print(max(dp[t-1]))