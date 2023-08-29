import sys
input = sys.stdin.readline

n = int(input())

L = []
for _ in range(n):
    L.append(int(input()))
L.sort()
preSum = L[:]
for i in range(1,n):
    preSum[i] += preSum[i-1]

dp = [L[0]] + [0] * (n-1)
if n == 1:
    print(0)
    exit(0)
if n >= 2:
    dp[1] = L[0]+L[1]
if n >= 3:
    dp[2] = 2*preSum[2]-L[2]

for i in range(3,n):
    dp[i] = min(dp[i-1]+preSum[i], dp[i-2]+2*preSum[i]-preSum[i-2])

print(dp[n-1])