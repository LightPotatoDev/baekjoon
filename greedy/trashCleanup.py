import sys
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
trash = sum([sum(grid[i]) for i in range(n)])
ans = 0

def check_down(y,x):
    trashY = []
    for i in range(y,n):
        if grid[i][x] == 1:
            trashY.append(i)
    return trashY

def cleanup():
    y = 0
    cleaned = 0

    for x in range(m):
        T = check_down(y,x)
        if T:
            y = T[-1]
        for i in T:
            grid[i][x] = 0
            cleaned += 1

    return cleaned

while trash > 0:
    trash -= cleanup()
    ans += 1

print(ans)
