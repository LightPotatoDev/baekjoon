import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
case = (n-2)*(m-2)
graph = [[[[11]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    #[redY][redX][blueY][blueX]
trace = [[[[""]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
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
graph[red[0]][red[1]][blue[0]][blue[1]] = 0

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
    for i in range(1,11):
        while dq:
            yr,xr,yb,xb = dq.popleft()
            for d in ["U","R","D","L"]:
                nyr,nxr,nyb,nxb = tilt(yr,xr,yb,xb,d)
                if graph[nyr][nxr][nyb][nxb] == 11:
                    graph[nyr][nxr][nyb][nxb] = i
                    trace[nyr][nxr][nyb][nxb] = trace[yr][xr][yb][xb] + d
                    nxt.append([nyr,nxr,nyb,nxb])
        dq = nxt.copy()
        nxt = deque()

bfs()
hy, hx = hole
ay, ax = 0,0
ans = 11
graph[hy][hx][hy][hx] = 11
for i,y in enumerate(graph[hy][hx]):
    for j,x in enumerate(y):
        if x < ans:
            ans = x
            ay,ax = i,j

if ans == 11:
    print(-1)
else:
    print(ans)
    print(trace[hy][hx][ay][ax])
