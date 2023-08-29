import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))[::-1]
dp = [[[0,0] for _ in range(n)] for _ in range(4)] #[player][turn][scoring]
#[player]: p1Max+p1Turn, p1Max+p2Turn, p2Max+p1Turn, p2Max+p2Turn
#[scoring]: p1Score, p2Score

dp[0][0] = [0,A[0]]
dp[1][0] = [A[0],0]
dp[2][0] = [0,A[0]]
dp[3][0] = [A[0],0]

for i in range(1,n):
    cases = [dp[j][i-1][:] for j in range(4)]

    dp[0][i] = max(cases, key=lambda x:x[0])
    dp[0][i][1] += A[i]

    dp[1][i] = max(cases, key=lambda x:x[0])
    dp[1][i][0] += A[i]

    dp[2][i] = max(cases, key=lambda x:x[1])
    dp[2][i][1] += A[i]

    dp[3][i] = max(cases, key=lambda x:x[1])
    dp[3][i][0] += A[i]

for i in dp:
    for j in i:
        print(j)
    print('')