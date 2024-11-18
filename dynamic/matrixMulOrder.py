import sys
input = sys.stdin.readline

n = int(input())
L = []
for i in range(n):
    a,b = map(int,input().split())
    if i == 0:
        L.append(a)
    L.append(b)

dp = [0]
for i in range(n):
    A = []
    for j in range(1,i+1):
        val = L[0]*L[j]*L[i+1]
        for k in range(i-j):
            val += L[j+k]*L[j+k+1]*L[i+1]
        A.append(dp[j] + val)
    dp.append(min(A,default = 0))
    print(A)
print(dp)
print(dp[n])

"""
Counter:
    1 10 / 10 1 / 1 3 / 3 2 / 2 1
    ans:19
    out:20
    모든 경우의 수를 커버하지 못함
    123 -> 345 -> 356 -> 136 순서가 정답
    위 dp는 123 -> 345 -> 135 순서에서 136 결과를 덧붙이기만 할 수 있음