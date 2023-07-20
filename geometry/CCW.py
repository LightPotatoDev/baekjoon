import math

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

theta1 = math.atan2(y2-y1,x2-x1)
theta2 = math.atan2(y3-y2,x3-x2)

angle = theta1 - theta2
if angle < 0 or angle > math.pi:
    print(1)
elif 0 < angle < math.pi:
    print(-1)
else:
    print(0)