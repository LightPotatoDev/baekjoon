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

    dirCross = vector.cross(b-a,d-c)

    if dirCross == 0:
        if vector.cross(c-a,b-a) == 0: #일직선
            a,b = swap(a,b)
            c,d = swap(c,d)
            if b==c or a==d:
                return 2
            else:
                return int(not (b<c or d<a))*4
        else:
            return 0 #평행

    p = (vector.cross(c-a,d-c) / dirCross)
    q = (vector.cross(c-a,b-a) / dirCross)

    if (p==0 or p==1) and (0<=q<=1):
        return 2
    else:
        return int(0<=p<=1 and 0<=q<=1)


T = int(input())

for _ in range(T):
    x3,y3,x4,y4 = map(int,input().split())
    x1,y1,x2,y2 = map(int,input().split())

    a = vector(x1,y1)
    b = vector(x2,y2)

    bl = vector(x3,y3)
    tl = vector(x3,y4)
    tr = vector(x4,y4)
    br = vector(x4,y3)

    rect = [bl,tl,tr,br]
    inter = [intersect(rect[i-1],rect[i],a,b) for i in range(4)]
    if any([i==4 for i in inter]):
        print(4)
    else:
        print(inter.count(1) + inter.count(2)//2)