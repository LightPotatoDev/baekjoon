import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0]*n for _ in range(n)]
board[0][0] = 2
for _ in range(k):
    y,x = map(int,input().split())
    board[y-1][x-1] = 1

l = int(input())
moves = deque([])
for _ in range(l):
    time, action = input().rstrip().split()
    moves.append([int(time), action])

dy = [0,1,0,-1]
dx = [1,0,-1,0]
rot = 0
snake = deque([[0,0]])

timeX = 0
nX, nr = moves.popleft()

def gameover(y,x):
    inbounds = (0 <= y < n) and (0 <= x < n)
    return (not inbounds) or (board[y][x] == 2)

while True:

    if timeX == nX:
        if nr == "D":
            rot = (rot+1) % 4
        else:
            rot = (rot-1) % 4

        if moves:
            nX, nr = moves.popleft()
        else:
            nX = 0
    timeX += 1
    ny,nx = snake[0][0]+dy[rot], snake[0][1]+dx[rot]

    if gameover(ny,nx):
        break
    snake.appendleft([ny,nx])
    if board[ny][nx] == 0:
        tailY, tailX = snake.pop()
        board[tailY][tailX] = 0
    board[ny][nx] = 2

print(timeX)

