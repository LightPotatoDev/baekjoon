import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
sy,sx,ey,ex = map(int,input().split())
grid = [input().rstrip() for _ in range(n)]

graph = [[[0]*m for _ in range(n)] for _ in range(4)] #[time][y][x]
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def ghost_sight(y,x,t,d):
    y += dy[d]
    x += dx[d]
    while 0 <= y < n and 0 <= x < m and grid[y][x] == '.':
        graph[t][y][x] = -1
        y += dy[d]
        x += dx[d]

for t in range(4):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                graph[t][i][j] = -1
            if grid[i][j].isnumeric():
                graph[t][i][j] = -1
                ghost_sight(i,j,t,(int(grid[i][j])+t)%4)

graph[0][sy-1][sx-1] = 1
to_visit = deque([(0,sy-1,sx-1)])
while to_visit:
    t,y,x = to_visit.popleft()
    nt = (t+1)%4
    for d in range(4):
        ny,nx = y+dy[d], x+dx[d]
        if 0 <= ny < n and 0 <= nx < m and graph[nt][ny][nx] == 0:
            to_visit.append((nt,ny,nx))
            graph[nt][ny][nx] = graph[t][y][x]+1
    if graph[nt][y][x] == 0:
        to_visit.append((nt,y,x))
        graph[nt][y][x] = graph[t][y][x]+1

res = [graph[t][ey-1][ex-1] for t in range(4)]
ans = int(1e9)
for r in res:
    if r >= 1:
        ans = min(ans, r)
print(ans-1 if ans != int(1e9) else 'GG')