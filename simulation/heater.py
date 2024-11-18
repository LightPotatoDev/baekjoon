import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
heaters = []
checks = []
for i in range(n):
    L = list(map(int,input().split()))
    for j in range(m):
        if 1 <= L[j] <= 4:
            heaters.append([i,j,L[j]])
        if L[j] == 5:
            checks.append([i,j])
temp = [[0]*m for _ in range(n)]
w = int(input())
walls = [[[0]*m for _ in range(n)] for _ in range(2)]
for _ in range(w):
    y,x,t = map(int,input().split())
    walls[t][y-1][x-1] = 1
ans = 0

dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]

def inbounds(y,x):
    return 0 <= y < n and 0 <= x < m

def wallcheck(y,x,ddy,ddx,d):
    if d == 1:
        if ddy == -1 and walls[1][y-1][x] == 0 and walls[0][y][x] == 0:
            return True
        if ddy == 0 and walls[1][y][x] == 0:
            return True
        if ddy == 1 and walls[1][y+1][x] == 0 and walls[0][y+1][x] == 0:
            return True

    if d == 2:
        if ddy == -1 and walls[1][y-1][x-1] == 0 and walls[0][y][x] == 0:
            return True
        if ddy == 0 and walls[1][y][x-1] == 0:
            return True
        if ddy == 1 and walls[1][y+1][x-1] == 0 and walls[0][y+1][x] == 0:
            return True

    if d == 3:
        if ddx == -1 and walls[0][y][x-1] == 0 and walls[1][y][x-1] == 0:
            return True
        if ddx == 0 and walls[0][y][x] == 0:
            return True
        if ddx == 1 and walls[0][y][x+1] == 0 and walls[1][y][x] == 0:
            return True

    if d == 4:
        if ddx == -1 and walls[0][y+1][x-1] == 0 and walls[1][y][x-1] == 0:
            return True
        if ddx == 0 and walls[0][y+1][x] == 0:
            return True
        if ddx == 1 and walls[0][y+1][x+1] == 0 and walls[1][y][x] == 0:
            return True

    return False


def heat(r,c,d):
    grid = [[0]*m for _ in range(n)]
    wind = [(r+dy[d],c+dx[d])]
    for lv in range(4):
        new_wind = []
        for y,x in wind:
            if inbounds(y,x):
                grid[y][x] = 5-lv

            for i in [-1,0,1]:
                ny = y+dy[d]+dx[d]*i
                nx = x+dx[d]+dy[d]*i
                if inbounds(ny,nx) and wallcheck(y,x,ny-y,nx-x,d):
                    new_wind.append((ny,nx))

            wind = new_wind[:]

    for y,x in wind:
        if inbounds(y,x):
            grid[y][x] = 1

    for i in range(n):
        for j in range(m):
            temp[i][j] += grid[i][j]

def adjust_temp():
    grid = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for dir in range(1,5):
                ny = i+dy[dir]
                nx = j+dx[dir]
                if inbounds(ny,nx) and temp[i][j] > temp[ny][nx] and wallcheck(i,j,ny-i,nx-j,dir):
                    adj = (temp[i][j] - temp[ny][nx]) // 4
                    grid[i][j] -= adj
                    grid[ny][nx] += adj

    for i in range(n):
        for j in range(m):
            temp[i][j] += grid[i][j]

def reduce_temp():
    for x in range(m-1):
        if temp[0][x] > 0:
            temp[0][x] -= 1
    for y in range(n-1):
        if temp[y][m-1] > 0:
            temp[y][m-1] -= 1
    for x in range(m-1,0,-1):
        if temp[n-1][x] > 0:
            temp[n-1][x] -= 1
    for y in range(n-1,0,-1):
        if temp[y][0] > 0:
            temp[y][0] -= 1

def check_temp():
    flag = True
    for y,x in checks:
        if temp[y][x] < k:
            flag = False
            break
    return flag

def print_temp():
    for i in temp:
        print(i)
    print('')

while ans <= 100:
    for y,x,d in heaters:
        heat(y,x,d)
    adjust_temp()
    reduce_temp()
    ans += 1
    if check_temp() == True:
        break

print(ans)