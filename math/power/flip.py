import sys
input = sys.stdin.readline

n,m = map(int,input().split())
L = [list(input().rstrip()) for _ in range(n)]
changeable = [[1]*m for _ in range(n)]

dy = [0,-1,0,1]
dx = [1,0,-1,0]

for i in range(n):
    for j in range(m):
        for dir in range(4):
            ny = i + dy[dir]
            nx = j + dx[dir]
            if (0 <= ny < n) and (0 <= nx < m) and (L[ny][nx] != L[i][j]):
                changeable[i][j] = 0
                break

s = sum([sum(changeable[i]) for i in range(n)])
print(pow(2,s,int(1e9)+7))
