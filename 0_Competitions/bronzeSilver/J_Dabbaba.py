import sys
input = sys.stdin.readline

n,k = map(int,input().split())

Dab = set()
Possible = set()

for _ in range(k):
    Dab.add(tuple(map(int,input().split())))

dx = [-2,0,2,0]
dy = [0,2,0,-2]

for d in Dab:
    x,y = d
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 < nx <= n and 0 < ny <= n and (nx,ny) not in Dab:
            Possible.add((nx,ny))

print(len(Possible))
