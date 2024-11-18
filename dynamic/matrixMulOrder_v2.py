import sys
input = sys.stdin.readline

n = int(input())
L = []
for i in range(n):
    a,b = map(int,input().split())
    if i == 0:
        L.append(a)
    L.append(b)

dp = [[0]*(n+1) for _ in range(n+1)] #[n][starting index]
for i in range(2,n+1):
    for j in range(i-2,-1,-1):
        dp[i][j] = min(dp[i-1][j] + L[j]*L[i]*L[i-1], dp[i][j+1] + L[j]*L[j+1]*L[i])

for i in dp:
    print(i)
print(dp[n][0])