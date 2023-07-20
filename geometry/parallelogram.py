xa,ya,xb,yb,xc,yc = map(int,input().split())

xPos = [xa,xb,xc]
yPos = [ya,yb,yc]

xd = [0,0,0]
yd = [0,0,0]

for i in range(3):
    xDiff = xPos[i%3]-xPos[(i+1)%3]
    yDiff = yPos[i%3]-yPos[(i+1)%3]

    xd[i] = xPos[(i+2)%3] + xDiff
    yd[i] = yPos[(i+2)%3] + yDiff

def getPerimeter(xS, yS):
    perimeter = 0
    print(xS,yS)
    for i in range(4):
        perimeter += ((xS[i-1]-xS[i])**2 + (yS[i-1]-yS[i])**2) ** 0.5
        print(perimeter)
    return perimeter

peris = []
for i in range(3):
    peris.append(getPerimeter(xPos+[xd[i]], yPos+[yd[i]]))

print(peris)
print(max(peris)-min(peris))