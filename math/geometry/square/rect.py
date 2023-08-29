x1,y1,p1,q1 = map(int,input().split())
x2,y2,p2,q2 = map(int,input().split())

dx = min(p1-x2,p2-x1)
dy = min(q2-y1,q1-y2)
if dx > 0 and dy > 0:
    print("FACE")
elif (dx == 0 and dy > 0) or (dx > 0 and dy == 0):
    print("LINE")
elif dx == 0 and dy == 0:
    print("POINT")
else:
    print("NULL")