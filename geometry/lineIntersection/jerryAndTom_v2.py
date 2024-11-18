import sys
input = sys.stdin.readline
from collections import deque

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

def point_on_line(p,a,b):
    if abs(p.x*(a.y - b.y) + a.x*(b.y - p.y) + b.x*(p.y - a.y)) != 0:
        return False
    if (min(a.x, b.x) <= p.x <= max(a.x, b.x)) and (min(a.y, b.y) <= p.y <= max(a.y, b.y)):
        return True

    return False

def can_reach_hole(mouse,hole):
    res = True
    for i in range(n):
        if intersect(mouse, hole, walls[i], walls[(i+1)%n]) != 0 and \
        point_on_line(hole,walls[i], walls[(i+1)%n]) == False:
            res = False
            break
    return res

def add_edge(u,v,c):
    capacity[u][v] = c
    adj[u].append(v)
    adj[v].append(u)

def network_flow(source, sink):
    total_flow = 0

    while True:
        parent = [-1]*(nc)
        dq = deque([source])

        while dq and parent[sink] == -1:
            u = dq.popleft()
            for v in adj[u]:
                if capacity[u][v] - flow[u][v] > 0 and parent[v] == -1:
                    parent[v] = u
                    dq.append(v)

        if parent[sink] == -1:
            break

        amount = int(1e10)
        v = sink
        while v != source:
            amount = min(amount, capacity[parent[v]][v]-flow[parent[v]][v])
            v = parent[v]

        v = sink
        while v != source:
            flow[parent[v]][v] += amount
            flow[v][parent[v]] -= amount
            v = parent[v]
        total_flow += amount

    return total_flow

n,k,h,m = map(int,input().split())
walls = []
holes = []
mice = []

nc = m+h+2
SRC = 0
SINK = nc-1
capacity = [[0]*nc for _ in range(nc)]
flow = [[0]*nc for _ in range(nc)]
adj = [[] for _ in range(nc)]

for _ in range(n):
    x,y = map(int,input().split())
    walls.append(Vector(x,y))
for _ in range(h):
    x,y = map(int,input().split())
    holes.append(Vector(x,y))
for _ in range(m):
    x,y = map(int,input().split())
    mice.append(Vector(x,y))

for i in range(m):
    for j in range(h):
        if can_reach_hole(mice[i], holes[j]):
            add_edge(i+1, m+j+1, 1)

for i in range(m):
    add_edge(SRC, i+1, 1)
for i in range(h):
    add_edge(m+i+1, SINK, k)

ans = network_flow(SRC,SINK)
if ans == m:
    print('Possible')
else:
    print('Impossible')