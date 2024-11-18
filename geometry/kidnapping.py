import sys
input = sys.stdin.readline

n = int(input())
y1,x1 = 0,0
y2,x2 = 0,0
L = []
for i in range(n):
    row = list(map(int,input().split()))
    for j,x in enumerate(row):
        if x == 5:
            y1,x1 = i,j
        elif x == 2:
            y2,x2 = i,j
    L.append(row)

cnt = 0
yi,xi = min(y1,y2), min(x1,x2)
yf,xf = max(y1,y2), max(x1,x2)
for i in range(yi,yf+1):
    for j in range(xi,xf+1):
        if L[i][j] == 1:
            cnt += 1

d = (y1-y2)**2 + (x1-x2)**2
if d >= 25 and cnt >= 3:
    print(1)
else:
    print(0)
