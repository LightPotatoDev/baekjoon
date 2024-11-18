from itertools import product
from copy import deepcopy

class CCTV:
    def __init__(self, data):
        self.type = data[0]
        self.yPos = data[1]
        self.xPos = data[2]

    def __repr__(self):
        return str([self.type,self.xPos,self.yPos])


n,m = map(int,input().split())
L = [[0]*m for _ in range(n)]
cctvs = []

for i in range(n):
    inp = list(map(int,input().split()))
    for j,x in enumerate(inp):
        if x == 6:
            L[i][j] = 6
        elif x != 0:
            cctvs.append(CCTV([x,i,j]))

DIR = [0,4,2,4,4,1]
dirTypes = []
for cctv in cctvs:
    dirTypes.append([i for i in range(DIR[cctv.type])])
comb = list(product(*dirTypes))

dy = [0,-1,0,1]
dx = [1,0,-1,0]

def findZone(dirs):

    def watch(cctv,dir):
        y = cctv.yPos
        x = cctv.xPos
        while (0 <= y < n) and (0 <= x < m) and (A[y][x] != 6):
            A[y][x] = 1
            y += dy[dir]
            x += dx[dir]

    A = deepcopy(L)
    for idx,cctv in enumerate(cctvs):
        if (cctv.type == 1):
            watch(cctv,dirs[idx])
        if (cctv.type == 2):
            watch(cctv,dirs[idx])
            watch(cctv,(dirs[idx]+2)%4)
        if (cctv.type == 3):
            watch(cctv,dirs[idx])
            watch(cctv,(dirs[idx]+1)%4)
        if (cctv.type == 4):
            watch(cctv,dirs[idx])
            watch(cctv,(dirs[idx]+1)%4)
            watch(cctv,(dirs[idx]+2)%4)
        if (cctv.type == 5):
            watch(cctv,dirs[idx])
            watch(cctv,dirs[idx]+1)
            watch(cctv,dirs[idx]+2)
            watch(cctv,dirs[idx]+3)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                cnt += 1
    return cnt

ans = 100
for c in comb:
    ans = min(findZone(c),ans)

print(ans)