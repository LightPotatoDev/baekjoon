import sys
input = sys.stdin.readline

n,m,q = map(int,input().split())

Row = [0]*n
Col = [0]*m
for _ in range(q):
    mode,rc,v = map(int,input().split())
    if mode == 1:
        Row[rc-1] += v
    else:
        Col[rc-1] += v

for i in range(n):
    for j in range(m):
        print(Row[i]+Col[j], end=' ')
    print('')