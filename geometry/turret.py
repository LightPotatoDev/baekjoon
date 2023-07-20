import math

T = int(input())

def dist(inp):
    x1, y1, r1, x2, y2, r2 = map(int, inp.split())
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if (x1 == x2) and (y1 == y2) and (r1 == r2):
        return -1
    elif (abs(r1-r2) < d < r1+r2):
        return 2
    elif (r1 + r2 == d) or (abs(r1-r2) == d):
        return 1
    else:
        return 0


for i in range(T):
    print(dist(input()))