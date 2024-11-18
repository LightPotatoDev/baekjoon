import sys
input = sys.stdin.readline

n,m = map(int,input().split())
Claps = [0]*(m+1)
for _ in range(n):
    row = list(map(int,input().split()))
    for i,x in enumerate(row):
        Claps[i+1] += x

for i in range(m):
    Claps[i+1] += Claps[i]

ans = 0
a = int(input())
for i in range(m-a+1):
    ans = max(ans,Claps[i+a]-Claps[i])

print(ans)
