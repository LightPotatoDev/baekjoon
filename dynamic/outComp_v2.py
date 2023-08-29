import sys
input = sys.stdin.readline

n = int(input())
T = []
P = []
for _ in range(n):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

money = [0]*n
for i in range(n-1,-1,-1):
    if i+T[i] <= n:
        money[i] = P[i]
        money[i] += max(money[i+T[i]:i+T[i]+51], default = 0)

    print(money)

print(max(money[:51]))