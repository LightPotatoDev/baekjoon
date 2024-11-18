import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    L = list(map(int,input().split()))
    S = [0]+L[:]
    dp = [[0]*n for _ in range(n)]

    for i in range(1,n+1):
        S[i] += S[i-1]

    for step in range(n-1):
        for i in range(n-step-1):
            j = i+step+1
            A = [dp[i][k+i]+dp[k+i+1][j] for k in range(step+1)]
            dp[i][j] = min(A)+S[j+1]-S[i]

    print(dp[0][n-1])