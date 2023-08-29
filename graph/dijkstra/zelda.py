import sys
import heapq
input = sys.stdin.readline

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def grid_dijkstra(start):
    hq = [start]
    cost = [[int(2e4)]*n for _ in range(n)]
    cost[0][0] = grid[0][0]

    while hq:
        w,y,x = heapq.heappop(hq)
        if cost[y][x] < w:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            inbounds = (0 <= ny < n) and (0 <= nx < n)
            if inbounds:
                newCost = cost[y][x] + grid[ny][nx]
                if newCost < cost[ny][nx]:
                    cost[ny][nx] = newCost
                    heapq.heappush(hq,(newCost,ny,nx))

    return cost[n-1][n-1]

c = 0
while True:
    c += 1
    n = int(input())
    if n == 0:
        break
    grid = [list(map(int,input().split())) for _ in range(n)]

    print(f"Problem {c}: {grid_dijkstra([grid[0][0],0,0])}")