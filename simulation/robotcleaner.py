n,m = map(int,input().split())
r,c,d = map(int,input().split())

room = []
for i in range(n):
    room.append(list(map(int,input().split())))

dy = [-1,0,1,0]
dx = [0,1,0,-1]
dir = d

def isCleanNear(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if room[ny][nx] == 0:
            return False
    return True

cleaned = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cleaned += 1
    elif isCleanNear(r,c) == True:
        ny = r - dy[dir]
        nx = c - dx[dir]
        if room[ny][nx] == 1:
            break
        else:
            r,c = ny,nx
    elif isCleanNear(r,c) == False:
        dir = (dir-1) % 4
        ny = r + dy[dir]
        nx = c + dx[dir]
        if room[ny][nx] == 0:
            r,c = ny,nx

print(cleaned)