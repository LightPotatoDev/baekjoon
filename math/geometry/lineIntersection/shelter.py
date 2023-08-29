from itertools import permutations, combinations
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

n = int(input())
bots =  [vector(*map(int,input().split())) for _ in range(n)]
shelt = [vector(*map(int,input().split())) for _ in range(n)]

N = [i for i in range(n)]
perm = permutations(N,n)

for sheltOrd in perm:
    flag = True
    comb = combinations(N,2)
    for i,j in comb:
        b1 = bots[i]
        s1 = shelt[sheltOrd[i]]
        b2 = bots[j]
        s2 = shelt[sheltOrd[j]]
        if intersect(b1,s1,b2,s2):
            flag = False
            break

    if flag == True:
        for i in sheltOrd:
            print(i+1)
        break
