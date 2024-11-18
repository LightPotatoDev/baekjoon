import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
grid = [[0]*n for _ in range(n)]
moves = [[0]*n for _ in range(n)]
search_order = []
dy = [0,-1,0,1]
dx = [1,0,-1,0]

for i in range(n):
    inp = list(map(int,input().split()))
    for j in range(n):
        grid[i][j] = inp[j]
        search_order.append([inp[j],i,j])
search_order.sort()

def inbounds(y,x):
    return 0 <= y < n and 0 <= x < n

def dfs(y,x,depth):
    moves[y][x] = depth
    for d in range(4):
        ny,nx = y + dy[d], x + dx[d]
        if inbounds(ny,nx) and moves[ny][nx] <= depth and grid[y][x] < grid[ny][nx]:
            dfs(ny,nx,depth+1)


for m,y,x in search_order:
    if moves[y][x] == 0:
        dfs(y,x,1)

print(max([max(moves[i]) for i in range(n)]))