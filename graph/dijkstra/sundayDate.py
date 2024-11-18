import sys
import heapq
input = sys.stdin.readline

def dijkstra(yi,xi,yf,xf):
    hq = [(0,yi,xi)]
    cost = [[int(1e8)] * m for _ in range(n)]
    cost[yi][xi] = 0

    while hq:
        w,y,x = heapq.heappop(hq)
        for dir in range(4):
            ny = y+dy[dir]
            nx = x+dx[dir]

            if not (0 <= nx < m and 0 <= ny < n):
                continue

            newCost = graph[ny][nx]+cost[y][x]
            if newCost < cost[ny][nx]:
                cost[ny][nx] = newCost
                heapq.heappush(hq,(newCost,ny,nx))


    return cost[yf][xf]

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
graph = [[0]*m for _ in range(n)]
yi,xi,yf,xf = 0,0,0,0

dx = [1,0,-1,0]
dy = [0,-1,0,1]
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            yi,xi = i,j
            continue
        if grid[i][j] == 'F':
            yf,xf = i,j
            continue
        if grid[i][j] == 'g':
            graph[i][j] = 10000
            continue

        for dir in range(4):
            nx = j+dx[dir]
            ny = i+dy[dir]
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if grid[ny][nx] == 'g':
                graph[i][j] = 1

ans = dijkstra(yi,xi,yf,xf)
print(ans//10000, ans%10000)

