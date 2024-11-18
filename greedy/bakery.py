import sys
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]

dy = [-1,0,1]
def install_pipes(y):
    pos = [y]
    for x in range(m-1):
        newPos = []
        for j in range(3):
            ny = y+dy[j]
            if 0 <= ny < n and grid[ny][x+1] != 'x':
                pos.append(ny)
                y = ny
                placed = True
                break

        if newPos == []:
            break
        pos = newPos[:]
    print(pos)
    return pos

ans = 0
for i in range(n):
    res = install_pipes(i)
    if res[0] != -1:
        ans += 1
        for x,y in enumerate(res):
            grid[y][x] = 'x'

    for i in grid:
        print(i)
    print('')
print(ans)