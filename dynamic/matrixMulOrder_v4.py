import sys
input = sys.stdin.readline

n = int(input())
L = []
for i in range(n):
    a,b = map(int,input().split())
    if i == 0:
        L.append(a)
    L.append(b)

dp = [[0]*(n+1) for _ in range(n)] #[n][starting index]
for i in range(n):
    for j in range(n-i-1):
        A = []
        for k in range(i+1):
            A.append(dp[k+j][j]+dp[i+j+1][k+j+1]+L[j]*L[j+k+1]*L[i+j+2])
        dp[i+j+1][j] = min(A)

print(dp[n-1][0])

"""
  for step in range(1, n):
        for i in range(n - step):
            j = i + step

by joonavel
대각선 방향 dp에서 덜 헷갈리기 위해 쓸 수도
"""