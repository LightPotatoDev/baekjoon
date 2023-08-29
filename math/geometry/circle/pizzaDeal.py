import math

a1,p1 = map(int,input().split())
r,p2 = map(int,input().split())
a2 = r**2*math.pi

if a1*p2 > a2*p1:
    print("Slice of pizza")
else:
    print("Whole pizza")