import sys
input = sys.stdin.readline

h,w = map(int,input().split())
y,x,d = map(int,input().split())

A = [list(map(int,list(input().rstrip()))) for _ in range(h)]
B = [list(map(int,list(input().rstrip()))) for _ in range(h)]
visited = [[0]*w for _ in range(h)]
movesLeft = h*w
moves = 0
ans = 0

dy = [-1,0,1,0]
dx = [0,1,0,-1]

while movesLeft > 0:
    moves += 1
    nd = (d + B[y][x]) % 4
    ny = y + dy[nd]
    nx = x + dx[nd]

    if visited[y][x] == 0:
        visited[y][x] = 1
        movesLeft = h*w*4
        ans = moves
        nd = (d + A[y][x]) % 4
        ny = y + dy[nd]
        nx = x + dx[nd]

    y = ny
    x = nx
    d = nd
    movesLeft -= 1

    if not ((0 <= y < h) and (0 <= x < w)):
        break

print(ans)