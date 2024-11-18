import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
grid = [input().rstrip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans = 0

def is_diamond(coords):
    if len(coords)%4 != 0:
        return False

    coords.sort(key = lambda x:(x[0],x[1]))
    top_y, top_x = coords[0]
    bot_y, bot_x = coords[-1]
    if top_x != bot_x:
        return False
    if (bot_y - top_y) % 2 != 0:
        return False
    size = (bot_y - top_y) // 2
    if len(coords)//4 != size:
        return False

    for i in range(size):
        y1,x1 = coords[1+2*i]
        y2,x2 = coords[2+2*i]
        if y1 != y2 or (x1 != top_x-(i+1)) or (x2 != top_x + (i+1)):
            return False

    for i in range(size-1):
        y1,x1 = coords[size*2+1+2*i]
        y2,x2 = coords[size*2+2+2*i]
        if y1 != y2 or (x1 != top_x-(size-i-1)) or (x2 != top_x + (size-i-1)):
            return False

    return True

dy = [0,-1,0,1]
dx = [1,0,-1,0]
def find_diamond(yi,xi):
    dq = deque([(yi,xi)])
    visited[yi][xi] = 1
    coords = []
    outside = False

    while dq:
        y,x = dq.popleft()
        for d in range(4):
            ny,nx = y+dy[d], x+dx[d]
            if not (0 <= ny < n and 0 <= nx < m):
                outside = True
                continue
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if grid[ny][nx] == '.':
                    dq.append((ny,nx))
                else:
                    coords.append((ny,nx))

    for y,x in coords:
        visited[y][x] = 0

    if outside == True:
        return 0

    return int(is_diamond(coords))


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and grid[i][j] == '.':
            ans += find_diamond(i,j)

print(ans)