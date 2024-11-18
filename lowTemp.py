import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]

def inbounds(y,x):
    return 0 <= y < n and 0 <= x < m

def check_recovery(y,x):
    ppl = 0
    for d in range(4):
        ny = y+dy[d]
        nx = x+dx[d]
        if not inbounds(ny,nx):
            continue
        if grid[ny][nx] == 'O':
            ppl += 1
    if ppl >= 2:
        return True
    else:
        return False

def add_nearby(y,x):
    for d in range(4):
        ny = y+dy[d]
        nx = x+dx[d]
        if not inbounds(ny,nx):
            continue
        if grid[ny][nx] == '.':
            near_rec.append((ny,nx))

dy = [0,-1,0,1]
dx = [1,0,-1,0]
near_rec = deque([])
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            if check_recovery(i,j) == True:
                grid[i][j] = 'O'
                add_nearby(i,j)

while near_rec:
    y,x = near_rec.popleft()
    if grid[y][x] == 'O':
        continue
    if check_recovery(y,x) == True:
        grid[y][x] = 'O'
        add_nearby(y,x)

def visit(i,j):
    to_visit = deque([(i,j)])
    while to_visit:
        y,x = to_visit.popleft()
        visited[y][x] = 1
        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]
            if not inbounds(ny,nx):
                continue
            if grid[ny][nx] == 'O' and visited[ny][nx] == 0:
                to_visit.append((ny,nx))

def check_square(i,j):
    width = 0
    height = 0
    y,x = i,j
    while x < m and grid[i][x] == 'O':
        width += 1
        x += 1
    while y < n and grid[y][j] == 'O':
        height += 1
        y += 1

    if min(width,height) <= k:
        return 0
    else:
        return width*height


visited = [[0]*m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and grid[i][j] == 'O':
            visit(i,j)
            ans += check_square(i,j)

print(ans)



