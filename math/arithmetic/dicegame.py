import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    L = list(map(int,input().split()))
    L.sort()
    a,b,c = L
    money = 0

    if a == b and b == c:
        money = 10000 + a*1000
    elif a == b or b == c:
        money = 1000 + b*100
    else:
        money = c*100

    ans = max(money,ans)
print(ans)