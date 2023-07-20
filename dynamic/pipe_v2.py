import sys
input = sys.stdin.readline

n = int(input())
board = []

def init(x):
    if x == '1':
        return [-1,0,0]
    else:
        return [0,0,0]

for _ in range(n):
    board.append(list(map(init,input().split())))
board[0][1] = [1,0,0]
#[가로 상태, 대각 상태, 세로 상태]

def placeable(y,x,rot):
    if board[y][x][0] == -1:
        return False
    if rot == 0:
        if board[y][x-1][0] == -1:
            return False
    elif rot == 1:
        if board[y-1][x-1][0] == -1 or board[y-1][x][0] == -1 or board[y][x-1][0] == -1:
            return False
    else:
        if board[y-1][x][0] == -1:
            return False
    return True

for i in range(n):
    for j in range(2,n):
        L = [0,0,0]
        if placeable(i,j,0):
            L[0] = board[i][j-1][0] + board[i][j-1][1]
        if i >= 1 and placeable(i,j,1):
            L[1] = board[i-1][j-1][0] + board[i-1][j-1][1] + board[i-1][j-1][2]
        if i >= 2 and placeable(i,j,2):
            L[2] = board[i-1][j][1] + board[i-1][j][2]
        if board[i][j][0] != -1:
            board[i][j] = L[:]

s = sum(board[n-1][n-1])
if s == -1:
    print(0)
else:
    print(s)