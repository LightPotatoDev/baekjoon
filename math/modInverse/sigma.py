import sys
input = sys.stdin.readline

m = int(input())
x = int(1e9)+7

q = 0
for _ in range(m):
    n,s = map(int,input().split())
    nInv = pow(n,-1,x)
    q = (q + (s*nInv)) % x
print(q)