import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    board = [[0]*n for _ in range(n)]
    start = list(map(int,input().split()))
    fin = list(map(int,input().split()))
    dq = deque([start])

    board[start[0]][start[1]] = 1
    dy = [-2,-1,1,2,2,1,-1,-2]
    dx = [1,2,2,1,-1,-2,-2,-1]

    while dq:
        p = dq.popleft()
        if p == fin:
            break
        for i in range(8):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]
            inbounds = 0 <= ny < n and 0 <= nx < n
            if inbounds and board[ny][nx] == 0:
                board[ny][nx] = board[p[0]][p[1]] + 1
                dq.append([ny,nx])

    print(board[fin[0]][fin[1]] - 1)

