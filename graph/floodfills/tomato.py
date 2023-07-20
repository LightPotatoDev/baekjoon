import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
L = []
starts = []
for i in range(m):
    line = list(map(int,input().rstrip().split()))
    for j,x in enumerate(line):
        if x == 1:
            starts.append([i,j])
    L.append(line)

dy = [-1,0,0,1]
dx = [0,-1,1,0]
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
            y,x = dq[0][0], dq[0][1]
            for i in range(4):
                if (0 <= y+dy[i] < m) and (0<= x+dx[i] < n):
                    if L[y+dy[i]][x+dx[i]] == 0:
                        upnext.append([y+dy[i],x+dx[i]])
                        L[y+dy[i]][x+dx[i]] = 1
            dq.popleft()
        if len(upnext) == 0:
            break
        step += 1
    return L,step

def checkzero(L):
    return any(0 in r for r in L)

finalL,ans = grid_bfs(L,starts)
if checkzero(finalL):
    print(-1)
else:
    print(ans)

