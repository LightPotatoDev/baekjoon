import sys
input = sys.stdin.readline

n,t = map(int,input().split())
City = [0] + [list(map(int,input().split())) for i in range(n)]

m = int(input())

def setDist(A,B):
    sa, xa, ya = A
    sb, xb, yb = B
    dist = abs(xa-xb) + abs(ya-yb)
    tele = t
    if sa != 1 or sb != 1:
        tele = 3000
    return min(dist,tele)

Special = []
for i,x in enumerate(City[1:]):
    if x[0] == 1:
        Special.append(i+1)

for _ in range(m):
    s,e = map(int,input().split())
    fromS = [0] * (n+1)
    fromE = [0] * (n+1)

    for i in range(1,n+1):
        fromS[i] = setDist(City[s],City[i])
    for i in range(1,n+1):
        fromE[i] = setDist(City[e],City[i])

    #1: 걸어 이동
    #2: 즉시 텔레포트
    #3: 걷기 -> 텔포 or 텔포 -> 걷기
    case123 = min([fromS[i]+fromE[i] for i in range(1,n+1)])
    #4: 걷기 -> 텔포 -> 걷기
    sToSpec = min([fromS[i] for i in Special])
    eToSpec = min([fromE[i] for i in Special])
    case4 = sToSpec + eToSpec + t
    print(min(case123,case4))