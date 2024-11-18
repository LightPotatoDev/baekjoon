import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(3e3))

class Node:
    def __init__(self,node_id,coords,is_land):
        self.node_id = node_id
        self.connection = []
        self.coords = coords
        self.is_land = is_land
        self.depth = 0
        self.visit_order = 0
        self.low = 0
        self.safe = True

    def __repr__(self):
        return f'Node ID: {self.node_id} \n\
connection: {self.connection} \n\
coords: {self.coords} \n\
is_land: {self.is_land} \n\
depth: {self.depth} \n\
visit_order: {self.visit_order}\n\
low: {self.low}\n\
safe: {self.safe}\n'

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
grid_visited = [[-1]*m for _ in range(n)]
assign_node_id = 0
nodes = []

dy = [0,-1,0,1]
dx = [1,0,-1,0]
def assign_node(y,x,icon):
    global assign_node_id
    to_visit = [(y,x)]
    coords = []
    connect = []

    while to_visit:
        i,j = to_visit.pop()
        coords.append((i,j))
        grid_visited[i][j] = assign_node_id
        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]
            if 0 <= nx < m and 0 <= ny < n:
                if grid_visited[ny][nx] == -1 and grid[ny][nx] == icon:
                    to_visit.append((ny,nx))
                elif grid_visited[ny][nx] != -1 and grid_visited[ny][nx] != assign_node_id:
                    connect.append(grid_visited[ny][nx])

    nodes.append(Node(assign_node_id, coords, icon=='#'))
    nodes[assign_node_id].connection = connect
    assign_node_id += 1

for i in range(n):
    for j in range(m):
        if grid_visited[i][j] == -1:
            assign_node(i,j,grid[i][j])

for no in nodes:
    for y,x in no.coords:
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nx < m and 0 <= ny < n and grid_visited[ny][nx] != no.node_id:
                no.connection.append(grid_visited[ny][nx])
    no.connection = set(no.connection)
    no.connection = list(no.connection)

time = 1
def dfs(u,par,depth):
    global time
    nodes[u].depth = depth
    nodes[u].visit_order = time
    nodes[u].low = time
    time += 1

    for v in nodes[u].connection:
        if nodes[v].visit_order == 0:
            dfs(v,u,depth+1)
            nodes[u].low = min(nodes[u].low, nodes[v].low)
        elif v != par:
            nodes[u].low = min(nodes[u].low, nodes[v].visit_order)

for i in range(len(nodes)):
    if nodes[i].visit_order == 0:
        dfs(i,-1,1)

def mark_unsafe(start_id):
    to_visit = [start_id]
    while to_visit:
        p = to_visit.pop()
        nodes[p].safe = False
        for v in nodes[p].connection:
            if nodes[v].safe == True and nodes[v].depth > nodes[p].depth:
                to_visit.append(v)

for no in nodes:
    if no.is_land and no.safe == True:
        for near in no.connection:
            if nodes[near].depth - no.depth == 1 and nodes[near].low >= no.visit_order and nodes[near].safe == True:
                mark_unsafe(near)

for no in nodes:
    if no.is_land and no.safe == True:
        for y,x in no.coords:
            grid[y][x] = 'O'
    elif no.is_land and no.safe == False:
        for y,x in no.coords:
            grid[y][x] = 'X'

for g in grid:
    print(''.join(g))