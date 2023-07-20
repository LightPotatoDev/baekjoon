import sys
from collections import deque
input = sys.stdin.readline

n,m,h = map(int,input().split())
L = [[] for _ in range(h)]
starts = []

for k in range(h):
    for i in range(m):
        line = list(map(int,input().rstrip().split()))
        for j,x in enumerate(line):
            if x == 1:
                starts.append([k,i,j])
        L[k].append(line)

dy = [-1,0,0,1,0,0]
dx = [0,-1,1,0,0,0]
dz = [0,0,0,0,1,-1]
def grid_bfs(L,starts):
    step = 0
    dq = deque()
    upnext = deque()
    for i in starts:
        upnext.append(i)

    while True:
        dq = upnext.copy()
        upnext = deque()
        while dq:
            z,y,x = dq[0][0], dq[0][1], dq[0][2]
            for i in range(6):
                nz = z+dz[i]
                ny = y+dy[i]
                nx = x+dx[i]

                if (0<= nz < h) and (0 <= ny < m) and (0<= nx < n):
                    if L[nz][ny][nx] == 0:
                        upnext.append([nz,ny,nx])
                        L[nz][ny][nx] = 1
            dq.popleft()
        if len(upnext) == 0:
            break
        step += 1
    return L,step

def checkzero(L):
    return any(0 in r for m in L for r in m)

finalL,ans = grid_bfs(L,starts)
if checkzero(finalL):
    print(-1)
else:
    print(ans)

