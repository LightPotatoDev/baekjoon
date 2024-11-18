import sys
input = sys.stdin.readline

class Vector:
    def __init__(self,xVal,yVal):
        self.x = xVal
        self.y = yVal

    def __repr__(self):
        return str([self.x,self.y])

    def __add__(self,v):
        return Vector(self.x+v.x, self.y+v.y)

    def __sub__(self,v):
        return Vector(self.x-v.x, self.y-v.y)

    def __mul__(self,a):
        return Vector(self.x*a, self.y*a)

    def __rmul__(self,a):
        return self*a

    def __lt__(self,v):
        return self.x < v.x or (self.x == v.x and self.y < v.y)

    def __gt__(self,v):
        return self.x > v.x or (self.x == v.x and self.y > v.y)

    def dot(self,v):
        return self.x*v.x + self.y+v.y

    def cross(self,v):
        return self.x*v.y - self.y*v.x

def intersect(a,b,c,d):
    dirCross = Vector.cross(b-a,d-c)

    if dirCross == 0:
        if Vector.cross(c-a,b-a) == 0: #일직선
            if a > b:
                a,b = b,a
            if c > d:
                c,d = d,c
            return not (b<c or d<a)
        else:
            return False #평행

    p = (Vector.cross(c-a,d-c) / dirCross)
    q = (Vector.cross(c-a,b-a) / dirCross)

    return 0<=p<=1 and 0<=q<=1

n = int(input())
lines = []
weights = []
for _ in range(n):
    x1,y1,x2,y2,w = map(int,input().split())
    v1 = Vector(x1,y1)
    v2 = Vector(x2,y2)
    lines.append((v1,v2))
    weights.append(w)

ans = 0
for i in range(n):
    for j in range(i+1,n):
        v1,v2 = lines[i]
        v3,v4 = lines[j]
        if intersect(v1,v2,v3,v4):
            ans += min(weights[i],weights[j])

print(ans+sum(weights))
