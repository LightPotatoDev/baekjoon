x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

d1 = x2-x1
d2 = y2-y1

if y3 <= y1 and y4 >= y2:
    if x3 >= x1 and x4 >= x2:
        d1 = min(x3-x1,d1)
    elif x3 <= x1 and x4 <= x2:
        d1 = min(x2-x4,d1)
    elif x3 <= x1 and x4 >= x2:
        d1 = 0

if x3 <= x1 and x4 >= x2:
    if y3 >= y1 and y4 >= y2:
        d2 = min(y3-y1,d2)
    elif y3 <= y1 and y4 <= y2:
        d2 = min(y2-y4,d2)
    elif y3 <= y1 and y4 >= y2:
        d2 = 0

print(d1*d2)

