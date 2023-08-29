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

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
a = vector(x1,y1)
b = vector(x2-x1,y2-y1)
c = vector(x3,y3)
d = vector(x4-x3,y4-y3)

def swap(p1,p2):
    if p1 > p2:
        return (p2,p1)
    else:
        return (p1,p2)

if vector.cross(b,d) == 0:
    if vector.cross((c-a),b) == 0:
        x1,x2 = swap(x1,x2)
        x3,x4 = swap(x3,x4)
        y1,y2 = swap(y1,y2)
        y3,y4 = swap(y3,y4)

        if x1 != x2:
            print(int(x1<=x3<=x2 or x1<=x4<=x2 or x3<=x1<=x4 or x3<=x2<=x4))
        else:
            print(int(y1<=y3<=y2 or y1<=y4<=y2 or y3<=y1<=y4 or y3<=y2<=y4))
        if x1 == x4:
            if y1 == y4:
                print(x1,y1)
            elif y2 == y3:
                print(x1,y2)
        elif x2 == x3:
            if y1 == y4:
                print(x2,y1)
            elif y2 == y3:
                print(x2,y2)
    else:
        print(0)
    exit()

p = (vector.cross((c-a),d) / vector.cross(b,d))
q = (vector.cross((c-a),b) / vector.cross(b,d))
if 0<=p<=1 and 0<=q<=1:
    print(1)
    ans = a+p*b
    print(ans.x, ans.y)
else:
    print(0)