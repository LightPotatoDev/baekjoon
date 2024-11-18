import sys
input = sys.stdin.readline

n = int(input())
L = []
for i in range(n):
    a,b = map(int,input().split())
    if i == 0:
        L.append(a)
    L.append(b)

def setDp(y,x):
    A = []
    for i in range(y-x-1):
        A.append(dp[y-i-1][x] + )
    return A

dp = [[0]*(n+1) for _ in range(n+1)] #[n][starting index]
for i in range(2,n+1):
    for j in range(i-2,-1,-1):
        A = [dp[i][j+1] + L[j]*L[j+1]*L[i]]
        A.extend(setDp(i,j))
        dp[i][j] = min(A)

for i in dp:
    print(i)
print(dp[n][0])