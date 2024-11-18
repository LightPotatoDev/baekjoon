from itertools import permutations

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

DIAG = 0.707106781186
def convert_to_points(L):
    dy = [0,-DIAG,-1,-DIAG,0,DIAG,1,DIAG]
    dx = [1,DIAG,0,-DIAG,-1,-DIAG,0,DIAG]
    points = []
    for i in range(8):
        points.append((L[i]*dy[i], L[i]*dx[i]))
    return points

stats = list(map(int,input().split()))
perm = permutations(stats,8)
ans = 0
for p in perm:
    flag = True
    points = convert_to_points(p)
    for i in range(8):
        if ccw(points[i-2], points[i-1], points[i]) != 1:
            flag = False
            break

    if flag == True:
        ans += 1

print(ans)