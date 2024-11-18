from itertools import combinations
from copy import deepcopy

n,m,h = map(int,input().split())
addLine = []
existLine = []

for i in range(h):
    for j in range(n-1):
        addLine.append((i+1,j+1))

for _ in range(m):
    a,b = map(int,input().split())
    existLine.append((a,b))
    for i in range(-1,2):
        if (a,b-i) in addLine:
            addLine.remove((a,b-i))

def drawable(c):
    l = len(c)
    if l <= 1:
        return True

    for i in range(l):
        y1,x1 = c[i]
        y2,x2 = c[(i+1)%l]
        if y1 == y2 and abs(x1-x2) == 1:
            return False

    return True

def ladderGame():
    for i in range(1,n+1):
        y,x = 1,i
        while y <= h:
            if (y,x) in existLine:
                x += 1
            elif (y,x-1) in existLine:
                x -= 1
            y += 1

        if x != i:
            return False

    return True


for i in range(4):
    comb = combinations(addLine,i)
    for c in comb:
        if not drawable(c):
            continue

        existLine.extend(c)
        if ladderGame() == True:
            print(len(c))
            exit(0)

        for j in range(len(c)):
            existLine.pop()

print(-1)
