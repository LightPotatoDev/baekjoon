x1,y1,r1 = map(int,input().split())
x2,y2,r2 = map(int,input().split())

dist = abs(x1-x2)**2 + abs(y1-y2)**2
r = (r1 + r2) ** 2

if dist >= r:
    print("NO")
else:
    print("YES")