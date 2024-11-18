import sys
import heapq
input = sys.stdin.readline

def dijkstra(yi,xi,yf,xf):
    hq = [(0,yi,xi)]
    cost = [[int(1e10)]*m for _ in range(n)]
    cost[yi][xi] = 0

    while hq:
        w,y,x = heapq.heappop(hq)
        if cost[y][x] < w:
            continue
        for nw,ny,nx in graph[y][x]:
            newCost = cost[y][x]+nw
            if newCost < cost[ny][nx]:
                cost[ny][nx] = newCost
                heapq.heappush(hq,(newCost,ny,nx))

    return cost[yf][xf]

n,m,t,d = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
graph = [[[] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j].islower():
            grid[i][j] = ord(grid[i][j]) - 71
        elif grid[i][j].isupper():
            grid[i][j] = ord(grid[i][j]) - 65

dy = [0,-1,0,1]
dx = [1,0,-1,0]
for y in range(n):
    for x in range(m):
        for dir in range(4):
            ny = y+dy[dir]
            nx = x+dx[dir]
            if not (0 <= ny < n and 0 <= nx < m):
                continue

            diff = grid[ny][nx] - grid[y][x]

            if -t <= diff <= 0:
                graph[y][x].append((1,ny,nx))
            elif 1 <= diff <= t:
                graph[y][x].append((diff**2,ny,nx))

ans = -1
for i in range(n):
    for j in range(m):
        cost = dijkstra(0,0,i,j) + dijkstra(i,j,0,0)
        if cost > d:
            continue
        ans = max(ans,grid[i][j])
print(ans)

