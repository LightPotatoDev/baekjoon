import math

x1,y1,r1,x2,y2,r2 = map(float,input().split())

d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if r1+r2 <= d:
    print('0.000');
    exit()
if d <= abs(r1-r2):
    print(round(min(r1,r2) ** 2 * math.pi, 3))
    exit()

a1 = math.acos((r1**2 + d**2 - r2**2)/(2*r1*d))
a2 = math.acos((r2**2 + d**2 - r1**2)/(2*r2*d))
s = (r1+r2+d) / 2
area1 = a1*r1*r1
area2 = a2*r2*r2
area3 = math.sqrt(s * (s-r1) * (s-r2) * (s-d)) * 2
print(round(area1 + area2 - area3,3))