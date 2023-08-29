import sys
input = sys.stdin.readline

L = [0]+list(input().rstrip())
n = len(L)-1

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][i] = 1
for i in range(1,n):
    dp[i][i+1] = int(L[i]==L[i+1])
for i in range(1,n-1):
    for j in range(1,n-i):
        dp[j][i+j+1] = int(dp[j+1][i+j]==1 and L[i+j+1] == L[j])

SE = []
for i in range(1,n+1):
    SE.append((dp[i].index(1), n-dp[i][::-1].index(1)))
SE.sort(key=lambda x:(x[1],x[0]))
end = SE[0][1]

cnt = 1
for i in range(1,n):
    if SE[i][0] > end:
        cnt += 1
        end = SE[i][1]
        print(SE[i])

print(cnt)