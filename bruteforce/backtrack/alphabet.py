import sys
input = sys.stdin.readline

r,c = map(int,input().split())
board = []
for _ in range(r):
    line = list(input().rstrip())
    board.append(line)

dy = [-1,0,1,0]
dx = [0,1,0,-1]
maxScore = 0

def alphaInd(y,x):
    return ord(board[y][x])-65

def move(y,x,score):
    global maxScore

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        inbounds = (0 <= ny < r) and (0 <= nx < c)

        if inbounds and visited[alphaInd(ny,nx)] == 0:
            visited[alphaInd(ny,nx)] = 1
            move(ny,nx,score+1)
            visited[alphaInd(ny,nx)] = 0

    maxScore = max(maxScore,score)

visited = [0]*26
visited[ord(board[0][0])-65] = 1
move(0,0,1)

print(maxScore)
