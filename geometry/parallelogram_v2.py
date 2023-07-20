xa,ya,xb,yb,xc,yc = map(int,input().split())

xPos = [xa,xb,xc]
yPos = [ya,yb,yc]

peris = []

for i in range(3):
    perimeter = 0
    for j in range(2):
        xLen = xPos[(i+j-1)%3]-xPos[(i+j)%3]
        yLen = yPos[(i+j-1)%3]-yPos[(i+j)%3]
        perimeter += 2 * (xLen ** 2 + yLen ** 2) ** 0.5
    peris.append(perimeter)

v1 = [xb-xa,yb-ya]
v2 = [xc-xb,yc-yb]
crossprod = v1[0]*v2[1] - v1[1]*v2[0]

if crossprod == 0:
    print(-1)
else:
    print(max(peris) - min(peris))