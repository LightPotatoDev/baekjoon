n = int(input())
N = (n*(n+1))//2
ans = N**2

xa,ya = map(int,input().split())
xb,yb = map(int,input().split())
adding = 0

if xa == xb:
    if ya > yb:
        ya,yb = yb,ya
    d = 0
    if (-1 <= ya <= n) or (-1 <= yb <= n):
        d = min(yb,n)-max(ya,-1)-1
    adding = (d*(d+1))//2
elif ya == yb:
    if xa > xb:
        xa,xb = xb,xa
    d = 0
    if (-1 <= xa <= n) or (-1 <= xb <= n):
        d = min(xb,n)-max(xa,-1)-1
    adding = (d*(d+1))//2

ans += (n+1) * adding

print(ans)