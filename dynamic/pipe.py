import sys
import copy
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

pipeState = [[0,1,0]]
#파이프 끝의 위치 / 회전 상태: 0-가로, 1-대각선, 2-세로

def placeable(y,x,rot):
    if rot == 0:
        if x < n-1 and board[y][x+1] == 0:
            if y == n-1 and x+1 == n-1:
                return 1
            else:
                return [y,x+1,0]
    elif rot == 1:
        if (x < n-1 and y < n-1):
            xCheck = board[y][x+1] == 0
            yCheck = board[y+1][x] == 0
            dCheck = board[y+1][x+1] == 0

            if xCheck and yCheck and dCheck:
                if y+1 == n-1 and x+1 == n-1:
                    return 1
                else:
                    return [y+1,x+1,1]
    else:
        if y < n-1 and board[y+1][x] == 0:
            if y+1 == n-1 and x == n-1:
                return 1
            else:
                return [y+1,x,2]

    return None

def appendDp(next):
    global cnt
    if next == 1:
        cnt += 1
    elif next != None:
        L.append(next)

cnt = 0
while pipeState:
    L = []
    for i in pipeState:
        if i[2] <= 1:
            appendDp(placeable(i[0],i[1],0))
        if i[2] >= 1:
            appendDp(placeable(i[0],i[1],2))
        appendDp(placeable(i[0],i[1],1))

    pipeState = copy.deepcopy(L)

print(cnt)