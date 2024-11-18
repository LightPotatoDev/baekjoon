import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
A.sort(key = lambda x:(x[0],x[1]))

s,e = -int(1e10), -int(1e10)
ans = 0
for i in range(n):
    a,b = A[i]
    if e < a:
        ans += e-s
        s = a
    e = max(e,b)

ans += e-s
print(ans)
