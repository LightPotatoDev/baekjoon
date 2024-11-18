import sys
input = sys.stdin.readline

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

ans = 0

dy = [-1,-1]
dx = [-1,1]

def placeable(y,x):
    for i in range(2):
        ny,nx = y+dy[i],x+dx[i]
        while (0 <= ny < n) and (0 <= nx < n):
            if L[ny][nx] == 2:
                return False
            ny,nx = ny+dy[i], nx+dx[i]
    return True

def nxt(i):
    if n%2 == 1:
        return 2
    else:
        if i%n == n-2:
            return 3
        elif i%n == n-1:
            return 1
        else:
            return 2

def place(ind,bishops):
    global ans
    if ind >= n**2:
        ans = max(ans,bishops)
        return

    y = ind // n
    x = ind % n
    if L[y][x] == 1 and placeable(y,x):
        L[y][x] = 2
        place(ind + nxt(ind), bishops+1)
        L[y][x] = 1
    place(ind + nxt(ind), bishops)

place(0,0)
place(1,ans)
print(ans)