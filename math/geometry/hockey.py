w,h,x,y,p = map(int,input().split())

players = []
for _ in range(p):
    players.append(list(map(int,input().split())))

def inRect(xPos,yPos):
    return (x <= xPos <= x+w) and (y <= yPos <= y+h)

def inCircle(mode,xPos,yPos):
    centerX, centerY = x+w*int(mode=="R"),y+h//2
    dist = (centerX-xPos)**2 + (centerY-yPos)**2

    return dist <= (h//2)**2

cnt = 0
for i in players:
    cnt += int(inRect(i[0],i[1]) or inCircle("L", i[0], i[1]) or inCircle("R", i[0],i[1]))
print(cnt)