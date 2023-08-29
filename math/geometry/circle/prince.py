import math

T = int(input())

def inside_circle(x, y, cx, cy, r):
    if math.sqrt((x-cx)**2 + (y-cy)**2) > r:
        return False
    return True

def trip():
    x1, y1, x2, y2 = map(int, input().split())
    planet_n = int(input())
    times = 0
    for i in range(planet_n):
        cx, cy, r = map(int, input().split())
        circ1 = inside_circle(x1, y1, cx, cy, r)
        circ2 = inside_circle(x2, y2, cx, cy, r)
        if circ1 != circ2:
            times += 1

    return times


for i in range(T):
    print(trip())