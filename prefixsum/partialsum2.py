import sys
input = sys.stdin.readline

n,m = map(int,input().split())
L = [0]+list(map(int,input().split()))
for i in range(1,n+1):
    L[i] += L[i-1]

cnt = 0
for i in range(n):
    for j in range(i+1,n+1):
        if L[j]-L[i] == m:
            cnt += 1
print(cnt)