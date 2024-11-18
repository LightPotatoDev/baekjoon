import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))

class Land:
    def __init__(self,land_id,coords,always_safe):
        self.land_id = land_id
        self.connection = []
        self.coords = coords
        self.always_safe = always_safe
        self.desc_safe = always_safe #the node has 'always_safe' descendant
        self.safe = always_safe
        self.depth = 0
        self.visit_order = 0
        self.low = 0

    def __repr__(self):
        return f'Land ID: {self.land_id} \n\
connection: {self.connection} \n\
coords: {self.coords} \n\
always_safe: {self.always_safe} \n\
desc_safe: {self.desc_safe} \n\
safe: {self.safe}\n\
depth: {self.depth}\n\
visit_order: {self.visit_order}\n\
low: {self.low}\n'

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
grid_visited = [[-1]*m for _ in range(n)]
assign_land_id = 1
lands = [0]

dy = [0,-1,0,1]
dx = [1,0,-1,0]
def assign_land(y,x,always_safe):
    global assign_land_id
    to_visit = [(y,x)]
    coords = []

    while to_visit:
        i,j = to_visit.pop()
        coords.append((i,j))
        grid_visited[i][j] = assign_land_id
        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]
            if 0 <= nx < m and 0 <= ny < n and grid_visited[ny][nx] == -1 and grid[ny][nx] == '#':
                to_visit.append((ny,nx))

    lands.append(Land(assign_land_id, coords, always_safe))
    assign_land_id += 1

def find_lands(y,x,always_safe):
    to_visit = [(y,x)]
    found_land = []
    nearby_land = set()
    prev_id = assign_land_id

    while to_visit:
        i,j = to_visit.pop()
        grid_visited[i][j] = 0
        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]
            if 0 <= nx < m and 0 <= ny < n:
                if grid_visited[ny][nx] == -1:
                    if grid[ny][nx] == '.':
                        to_visit.append((ny,nx))
                    elif grid[ny][nx] == '#':
                        found_land.append(assign_land_id)
                        assign_land(ny,nx,always_safe)
                if 0 < grid_visited[ny][nx] < prev_id:
                    nearby_land.add(grid_visited[ny][nx])

    for f in found_land:
        for ne in nearby_land:
            lands[f].connection.append(ne)
            lands[ne].connection.append(f)

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' and grid_visited[i][j] == -1:
            find_lands(i,j,assign_land_id == 1)

time = 1
visit_hist = [0]
def dfs(u,par,depth):
    global time
    lands[u].depth = depth
    lands[u].visit_order = time
    lands[u].low = time
    visit_hist.append(u)
    time += 1

    for v in lands[u].connection:
        if lands[v].visit_order == 0:
            dfs(v,u,depth+1)
            lands[u].low = min(lands[u].low, lands[v].low)
            if lands[v].desc_safe:
                lands[u].desc_safe = True
        elif v != par:
            lands[u].low = min(lands[u].low, lands[v].visit_order)

for i in range(1,len(lands)):
    if lands[i].visit_order == 0:
        dfs(i,-1,1)

for l in lands[1:]:
    if l.desc_safe or l.depth - lands[visit_hist[l.low]].depth >= 2:
        l.safe = True

for l in lands[1:]:
    if l.safe == True:
        for y,x in l.coords:
            grid[y][x] = 'O'
    else:
        for y,x in l.coords:
            grid[y][x] = 'X'

for g in grid:
    print(''.join(g))