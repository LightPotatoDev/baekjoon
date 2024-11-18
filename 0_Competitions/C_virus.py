import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tg,tb,x,b = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
virus = []
build_vir = [[] for _ in range(tg)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            virus.append((i,j))

dy = [0,-1,0,1]
dx = [1,0,-1,0]
def inbounds(y,x):
    return 0 <= y < n and 0 <= x < m

def spread(t):
    global virus
    new_virus = []
    for y,x in virus:
        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]
            if not inbounds(ny,nx):
                continue
            if grid[ny][nx] == '.':
                new_virus.append((ny,nx))
                grid[ny][nx] = '*'
            if grid[ny][nx] == '#':
                if t+tb < tg:
                    build_vir[t+tb].append((ny,nx))
                grid[ny][nx] = '='
    virus = new_virus

def print_grid():
    for i in grid:
        print(i)
    print('')

for t in range(tg):
    spread(t)
    for y,x in build_vir[t]:
        virus.append((y,x))
        grid[y][x] = '*'

ans = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' or grid[i][j] == '=' or grid[i][j] == '#':
            ans.append((i+1,j+1))
if ans:
    for y,x in ans:
        print(y,x)
else:
    print(-1)
