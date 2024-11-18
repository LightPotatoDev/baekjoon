import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def grid_bfs(yi,xi):
    dq = deque([[yi,xi]])
    visited = [[0]*m for _ in range(n)]
    visited[yi][xi] = 1
    steps = 0

    while dq:
        y,x = dq.popleft()

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if not ((0 <= ny < n) and (0 <= nx < m)):
                continue

            if (L[ny][nx] == 'L') and (visited[ny][nx] == 0):
                dq.append([ny,nx])
                visited[ny][nx] = visited[y][x] + 1
                steps = max(steps, visited[ny][nx])

    return steps-1


n,m = map(int,input().split())
L = [list(input().rstrip()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if (L[i][j] == 'L'):
            ans = max(ans,grid_bfs(i,j))

print(ans)

