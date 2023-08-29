import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))[::-1]
dp = [[[0 for _ in range(2)] for _ in range(4)] for _ in range(n)] #[turn][player][scoring]
#[player]: p1Max+p1Turn, p1Max+p2Turn, p2Max+p1Turn, p2Max+p2Turn
#[scoring]: p1Score, p2Score

dp[0][0] = [0,A[0]]
dp[0][1] = [A[0],0]
dp[0][2] = [0,A[0]]
dp[0][3] = [A[0],0]

for i in range(1,n):
    cases = [dp[i-1][j] for j in range(4)]

    for j in range(4):
        goodCase = max(cases, key=lambda x:x[j//2])
        for k in range(2):
            dp[i][j][k] = goodCase[k]
        dp[i][j][(j-1)%2] += A[i]
        print(dp[i])

for i in dp:
    for j in i:
        print(j)
    print('')