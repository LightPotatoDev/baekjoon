import sys
input = sys.stdin.readline

class vector:
    def __init__(self,p1,p2):
        self.x = p2[0]-p1[0]
        self.y = p2[1]-p1[1]
        self.z = p2[2]-p1[2]

    def __repr__(self):
        return str([self.x,self.y,self.z])

def vLen(v):
    return ( v.x**2 + v.y**2 + v.z**2 )**0.5

def dotProd(v1,v2):
    return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z

def crossProd(v1,v2):
    v = [v1.y*v2.z-v2.y*v1.z, v2.x*v1.z-v1.x*v2.z, v1.x*v2.y-v2.x*v1.y]
    return vector([0,0,0],v)

ax,ay,az,bx,by,bz,cx,cy,cz = map(int,input().split())
u = vector([ax,ay,az],[bx,by,bz])
uR = vector([bx,by,bz],[ax,ay,az])
v1 = vector([ax,ay,az],[cx,cy,cz])
v2 = vector([bx,by,bz],[cx,cy,cz])

a1 = dotProd(u,v1) / (vLen(u) * vLen(v1))
a2 = dotProd(uR,v2) / (vLen(u) * vLen(v2))
d = int(1e10)
if a1 >= 0 and a2 >= 0:
    d = vLen(crossProd(u,v1)) / vLen(u)
print(min([vLen(v1), vLen(v2), d]))