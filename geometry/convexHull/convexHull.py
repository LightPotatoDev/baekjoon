import sys
input = sys.stdin.readline

def ccw(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3

    v1 = [x2-x1,y2-y1]
    v2 = [x3-x2,y3-y2]
    crossprod = v1[0]*v2[1] - v1[1]*v2[0]

    if crossprod < 0:
        return -1
    elif crossprod == 0:
        return 0
    else:
        return 1

n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
points.sort(key=ccw)
print(points)