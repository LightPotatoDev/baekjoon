import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))[::-1]
dp = [[[0,0,0] for _ in range(n)] for _ in range(2)] #[curPlayer][turn][scoring]
#[scoring]: p1Score, p2Score, scoreDiff

dp[0][0] = [0,A[0],abs(A[0])]
dp[1][0] = [A[0],0,abs(A[0])]

for i in range(1,n):
    c1 = dp[0][i-1][:]
    c1[1] += A[i]
    c1[2] = abs(c1[0]-c1[1])

    c2 = dp[1][i-1][:]
    c2[1] += A[i]
    c2[2] = abs(c2[0]-c2[1])

    dp[0][i] = max([c1,c2], key=lambda x: x[0])

    c1 = dp[0][i-1][:]
    c1[0] += A[i]
    c1[2] = abs(c1[0]-c1[1])

    c2 = dp[1][i-1][:]
    c2[0] += A[i]
    c2[2] = abs(c2[0]-c2[1])

    dp[1][i] = max([c1,c2], key=lambda x: x[1])

for i in dp:
    for j in i:
        print(j)
    print('')