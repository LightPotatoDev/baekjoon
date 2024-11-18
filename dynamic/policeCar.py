import sys
input = sys.stdin.readline

n = int(input())
w = int(input())
Case = [[0,0]]+[list(map(int,input().split())) for _ in range(w)]

dp = [[0]*(w*2) for _ in range(w)]

def dist(ci,cf,moving):
    xf,xi = Case[cf][0],Case[ci][0]
    yf,yi = Case[cf][1],Case[ci][1]

    if ci == 0 and moving == 1:
        xi,yi = 1,1
    if ci == 0 and moving == 2:
        xi,yi = n,n

    return abs(xf-xi) + abs(yf-yi)

dp[0][0] = [dist(0,1,1),-1]
dp[0][1] = [dist(0,1,2),-1]

for i in range(1,w):
    for j in range(i):
        dp[i][j] = [dp[i-1][j][0]+dist(i,i+1,1), j]

    j = i
    for k in range(i,i*2):
        if dp[i][j] == 0 or dp[i][j][0] > dp[i-1][k][0] + dist(2*i-k-1,i+1,1):
            dp[i][j] = [dp[i-1][k][0] + dist(2*i-k-1,i+1,1),k]

    j = i+1
    for k in range(i):
        if dp[i][j] == 0 or dp[i][j][0] > dp[i-1][k][0] + dist(k,i+1,1):
            dp[i][j] = [dp[i-1][k][0] + dist(k,i+1,2),k]

    for j in range(i+2,2*i+2):
        dp[i][j] = [dp[i-1][j-2][0]+dist(i,i+1,2), j-2]

ans = min(dp[w-1], key=lambda x:x[0])
print(ans[0])

trace = []
back = dp[w-1].index(ans)

for i in range(w-1,-1,-1):
    trace.append(back//(i+1) + 1)
    back = dp[i][back][1]

for i in trace[::-1]:
    print(i)

##print(trace)
##for row in dp:
##    print(row)