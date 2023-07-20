import sys
input = sys.stdin.readline

n,m = map(int,input().split())
L = list(map(int,input().split()))
for i in range(1,len(L)):
    L[i] += L[i-1]

for _ in range(m):

    x,y = map(int,input().split())
    if x != 1:
        print(L[y-1]-L[x-2])
    else:
        print(L[y-1])
