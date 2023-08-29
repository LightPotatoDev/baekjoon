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
for i in range(n):
    if i+T[i] <= n:
        okDay = []
        start = (i-50) * int(i >= 50)
        for j in range(start,i):
            if i-j-T[j] >= 0:
                okDay.append(money[j])
        money[i] = max(okDay, default=0) + P[i]

print(max(money[-50:]))