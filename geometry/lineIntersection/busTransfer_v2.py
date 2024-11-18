import sys
from itertools import combinations
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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1
        self.size = 1

    def find(self):
        root = self
        while root != root.next:
            root = root.next
        return root

    def union(self, node):
        root1 = self.find()
        root2 = node.find()
        if root1 == root2:
            return

        if root1.rank >= root2.rank:
            root2.next = root1
            root1.size += root2.size
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2
            root2.size += root1.size

    def __repr__(self):
        return str(self.data)

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
L = [Node(i) for i in range(n)]
lines = [[i]+list(map(int,input().split())) for i in range(n)]
comb = combinations(lines,2)

for l1,l2 in comb:
    n1,x1,y1,x2,y2 = l1
    n2,x3,y3,x4,y4 = l2
    a = Vector(x1,y1)
    b = Vector(x2,y2)
    c = Vector(x3,y3)
    d = Vector(x4,y4)
    if intersect(a,b,c,d):
        L[n1].union(L[n2])

maxSize = 0
roots = set()
for i in range(n):
    root = L[i].find()
    roots.add(root)
    maxSize = max(maxSize, root.size)
print(len(roots))
print(maxSize)