import sys
input = sys.stdin.readline

n,k,b = map(int,input().split())

L = [0]*(n+1)
for _ in range(b):
    L[int(input())] = 1

for i in range(1,n+1):
    L[i] += L[i-1]

ans = 9999999
for i in range(k,n+1):
    ans = min(ans,L[i]-L[i-k])

print(ans)