import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[[[int(1e5)]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    #[redY][redX][blueY][blueX]
board = []
red = []
blue = []
hole = []

for i in range(n):
    row = list(input().rstrip())
    for j in range(m):
        if row[j] == "B":
            blue = [i,j]
            row[j] = "."
        elif row[j] == "R":
            red = [i,j]
            row[j] = "."
        elif row[j] == "O":
            hole = [i,j]
            row[j] = "."
    board.append(row)

Direction = {"U":[-1,0], "R":[0,1], "D":[1,0], "L":[0,-1]}
def tilt(yr,xr,yb,xb,dir):
    moved = True
    dy,dx = Direction[dir]
    while moved:
        moved = False
        wallColR = board[yr+dy][xr+dx] == "#"
        wallColB = board[yb+dy][xb+dx] == "#"
        redCol   = [yb+dy,xb+dx] == [yr,xr]
        blueCol  = [yr+dy,xr+dx] == [yb,xb]
        redHole  = [yr,xr] == hole
        blueHole = [yb,xb] == hole

        if (not wallColR) and ((not blueCol) or blueHole) and (not redHole):
            yr += dy
            xr += dx
            moved = True
        if (not wallColB) and ((not redCol) or redHole) and (not blueHole):
            yb += dy
            xb += dx
            moved = True

    return (yr,xr,yb,xb)

def bfs():
    dq = deque([red+blue])
    nxt = deque()
    i = 0
    while True:
        i += 1
        while dq:
            yr,xr,yb,xb = dq.popleft()
            for d in ["U","R","D","L"]:
                nyr,nxr,nyb,nxb = tilt(yr,xr,yb,xb,d)
                if graph[nyr][nxr][nyb][nxb] == int(1e5):
                    graph[nyr][nxr][nyb][nxb] = i
                    nxt.append([nyr,nxr,nyb,nxb])
        if not nxt:
            break
        dq = nxt.copy()
        nxt = deque()

bfs()
hx, hy = hole
ans = int(1e5)
graph[hx][hy][hx][hy] = int(1e5)
for i in graph[hx][hy]:
    ans = min(min(i),ans)
if ans == int(1e5):
    print(-1)
else:
    print(ans)
