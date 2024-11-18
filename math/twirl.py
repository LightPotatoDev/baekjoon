r1,c1,r2,c2 = map(int,input().split())
L = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]

dy = [-1,0,1,0]
dx = [0,-1,0,1]

def getTwirl(r,c):
    layer = max(abs(r),abs(c))
    y,x = layer,layer
    n = 1
    m = (2*layer-1)**2

    for i in range(4):
        for j in range(layer*2):
            y += dy[i]
            x += dx[i]
            m += 1
            if y == r and x == c:
                n = m

    return n


for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        L[i][j] = getTwirl(r1+i, c1+j)

maxNum = max([max(row) for row in L])
maxLen = len(str(maxNum))

for row in L:
    for i in row:
        print("{:>{}}".format(i,maxLen), end=' ')
    print('')