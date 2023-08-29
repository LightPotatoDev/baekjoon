import sys
input = sys.stdin.readline

class vector:
    def __init__(self,xVal,yVal):
        self.x = xVal
        self.y = yVal

    def __repr__(self):
        return str([self.x,self.y])

    def __add__(self,v):
        return vector(self.x+v.x, self.y+v.y)

    def __sub__(self,v):
        return vector(self.x-v.x, self.y-v.y)

    def __mul__(self,a):
        return vector(self.x*a, self.y*a)

    def __rmul__(self,a):
        return self*a

    def __truediv__(self,a):
        return vector(self.x/a, self.y/a)

    def __lt__(self,v):
        return self.x < v.x or (self.x == v.x and self.y < v.y)

    def __gt__(self,v):
        return self.x > v.x or (self.x == v.x and self.y > v.y)

    def dot(self,v):
        return self.x*v.x + self.y+v.y

    def cross(self,v):
        return self.x*v.y - self.y*v.x

    def len(self):
        return (self.x**2 + self.y**2)**0.5

def ccw(p,a,b):
    return (a-p).cross(b-p)

def swap(p1,p2):
    if p2 < p1:
        return (p2,p1)
    else:
        return (p1,p2)

def intersect(p,q,r,s):
    pq = ccw(p,q,r)*ccw(p,q,s)
    rs = ccw(r,s,p)*ccw(r,s,q)
    if pq == 0 and rs == 0:
        p,q = swap(p,q)
        r,s = swap(r,s)
        return not (q<r or s<p)
    return pq<=0 and rs<=0

T = int(input())

for _ in range(T):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())
    x3,x4 = swap(x3,x4)
    y3,y4 = swap(y3,y4)

    if (x3<=x1<=x4 and y3<=y1<=y4) or (x3<=x2<=x4 and y3<=y2<=y4):
        print("T")
        continue

    a = vector(x1,y1)
    b = vector(x2,y2)

    bl = vector(x3,y3)
    tl = vector(x3,y4)
    tr = vector(x4,y4)
    br = vector(x4,y3)

    rect = [bl,tl,tr,br]
    inter = [intersect(rect[i-1],rect[i],a,b) for i in range(4)]

    if any(inter):
        print("T")
    else:
        print("F")