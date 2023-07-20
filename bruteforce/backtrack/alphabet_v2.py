import sys
input = sys.stdin.readline

r,c = map(int,input().split())
board = []
for _ in range(r):
    board.append(input().rstrip())

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def alphaInd(y,x):
    return ord(board[y][x])-65

maxScore = 0
visited = [0]*26

def grid_dfs(y,x,score):
    global maxScore
    visited[alphaInd(y,x)] = 1
    adj = []

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < r) and (0 <= nx < c):
            adj.append([ny,nx])

    for i,j in adj:
        if visited[alphaInd(i,j)] == 0:
            grid_dfs(i,j,score + 1)

    visited[alphaInd(y,x)] = 0
    maxScore = max(maxScore, score)

grid_dfs(0,0,1)
print(maxScore)