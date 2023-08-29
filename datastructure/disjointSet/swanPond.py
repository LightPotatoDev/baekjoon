import sys
input = sys.stdin.readline
from collections import deque

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

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def grid_bfs(start,areaID):
    dq = deque([start])
    yi,xi = start
    hasSwan = L[yi][xi] == "L"
    L[yi][xi] = areaID

    while dq:
        y,x = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds and (L[ny][nx] == "." or L[ny][nx] == "L"):
                if L[ny][nx] == "L":
                    hasSwan = True
                L[ny][nx] = areaID
                dq.append([ny,nx])
            elif inbounds and L[ny][nx] == "X":
                L[ny][nx] = "M"
                melting.add((ny,nx))

    return hasSwan

def meltIce():
    global melting
    newMelt = set()

    for icePos in melting:
        y,x = icePos
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < m)
            if inbounds and L[ny][nx] == "X":
                L[ny][nx] = "M"
                newMelt.add((ny,nx))
            elif inbounds and type(L[ny][nx]) == int:
                if L[y][x] == "M":
                    areaNum = L[ny][nx]
                    L[y][x] = areaNum
                else:
                    myID = L[y][x]
                    otherID = L[ny][nx]
                    N[myID].union(N[otherID])

    melting = newMelt

n,m = map(int,input().split())
L = []
melting = set()
swans = []
N = []
for _ in range(n):
    L.append(list(input().strip()))


areaID = 0
for i in range(n):
    for j in range(m):
        if L[i][j] == "." or L[i][j] == "L":
            node = Node(areaID)
            N.append(node)
            hasSwan = grid_bfs([i,j],areaID)

            if hasSwan:
                swans.append(node)

            areaID += 1

if len(swans) == 1:
    print(0)
    exit()

days = 0
while True:
    meltIce()
    days += 1
    if swans[0].find() == swans[1].find():
        print(days)
        break

