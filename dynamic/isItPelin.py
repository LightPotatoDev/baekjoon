import sys
input = sys.stdin.readline

n = int(input())
L = [0]+list(map(int,input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][i] = 1
for i in range(1,n):
    dp[i][i+1] = int(L[i]==L[i+1])
for i in range(1,n-1):
    for j in range(1,n-i):
        dp[j][i+j+1] = int(dp[j+1][i+j]==1 and L[i+j+1] == L[j])

m = int(input())
for _ in range(m):
    s,e = map(int,input().split())
    print(dp[s][e])