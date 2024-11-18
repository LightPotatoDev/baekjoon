import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
target = [list(map(int,input().split())) for _ in range(n)]
diff = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        diff[i][j] = grid[i][j] - target[i][j]
volcano = [[0]*m for _ in range(n)]
for _ in range(k):
    y,x = map(int,input().split())
    volcano[y-1][x-1] = 1

for i in diff:
    print(i)