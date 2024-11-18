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

    def __truediv__(self,a):
        return Vector(self.x/a, self.y/a)

    def __lt__(self,v):
        return self.x < v.x or (self.x == v.x and self.y < v.y)

    def __gt__(self,v):
        return self.x > v.x or (self.x == v.x and self.y > v.y)

    def __eq__(self,v):
        return self.x == v.x and self.y == v.y

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

#0:만나지 않음, 1:선분의 중간, 2:선분의 끝, 4:교점 무한
def intersect(a,b,c,d):

    dirCross = Vector.cross(b-a,d-c)

    if dirCross == 0:
        if Vector.cross(c-a,b-a) == 0: #일직선
            a,b = swap(a,b)
            c,d = swap(c,d)
            if b==c or a==d:
                return 2
            else:
                return int(not (b<c or d<a))*4
        else:
            return 0 #평행

    p = (Vector.cross(c-a,d-c) / dirCross)
    q = (Vector.cross(c-a,b-a) / dirCross)

    if (p==0 or p==1) and (0<=q<=1):
        return 2
    else:
        return int(0<=p<=1 and 0<=q<=1)

def tri_area(p,a,b):
    return abs(p.x*(a.y - b.y) + a.x*(b.y - p.y) + b.x*(p.y - a.y))

def point_on_line(p,a,b):
    if tri_area(p,a,b) != 0:
        return False
    if (min(a.x, b.x) <= p.x <= max(a.x, b.x)) and (min(a.y, b.y) <= p.y <= max(a.y, b.y)):
        return True

    return False

tri = []
for _ in range(3):
    x,y = map(int,input().split())
    tri.append(Vector(x,y))

n = int(input())
ans = 0
for _ in range(n):
    x,y = map(int,input().split())
    v1 = Vector(x,y)
    v2 = Vector(x+1, y + 1e6+2)
    inter = 0
    on_line = False
    for i in range(3):
        p1,p2 = tri[i], tri[(i+1)%3]
        if intersect(v1,v2,p1,p2) > 0:
            inter += 1
        if point_on_line(v1,p1,p2):
            on_line = True
    if inter%2 == 1 or on_line == True:
        ans += 1

print(tri_area(tri[0],tri[1],tri[2]) / 2)
print(ans)