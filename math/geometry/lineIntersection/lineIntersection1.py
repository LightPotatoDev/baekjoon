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

if vector.cross(b,d) == 0:
    print(0)
    exit()
p = (vector.cross((c-a),d) / vector.cross(b,d))
q = (vector.cross((c-a),b) / vector.cross(b,d))
print(int(0<=p<=1 and 0<=q<=1))