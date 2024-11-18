import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.rank = 1

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
            if root1.rank == root2.rank:
                root1.rank += 1
        else:
            root1.next = root2

    def __repr__(self):
        return str(self.data)

n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]

dy = [-1,0,0,1]
dx = [0,-1,1,0]

areas = []
areaID = 2

def grid_bfs(start,areaID):
    dq = deque([start])
    L[start[0]][start[1]] = areaID
    pos = []
    while dq:
        y,x = dq.popleft()
        pos.append([y,x])

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds and L[ny][nx] == 1:
                L[ny][nx] = areaID
                dq.append([ny,nx])

    areas.append([areaID,pos])

for i in range(n):
    for j in range(m):
        if L[i][j] == 1:
            grid_bfs([i,j],areaID)
            areaID += 1

def inbounds(y,x):
    return (0 <= y < n) and (0 <= x < m)

def makeBridge(a1,a2):
    dist = 999
    for pos in a1[1]:
        y,x = pos
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            d = 0
            while inbounds(ny,nx) and L[ny][nx] == 0:
                d += 1
                ny,nx = ny+dy[i], nx+dx[i]
                if inbounds(ny,nx) and L[ny][nx] == a2[0]:
                    if d >= 2:
                        dist = min(dist,d)
                    break

    if dist != 999:
        graph.append([a1[0],a2[0],dist])


graph = []
comb = combinations(areas,2)

for a1,a2 in comb:
    makeBridge(a1,a2)
graph.sort(key=lambda x:x[2])

N = [Node(i) for i in range(len(areas))]
ans = 0
for a,b,c in graph:
    if N[a-2].find() != N[b-2].find():
        N[a-2].union(N[b-2])
        ans += c

sample = N[0].find()
for node in N:
    if node.find() != sample:
        print(-1)
        exit()
print(ans)
