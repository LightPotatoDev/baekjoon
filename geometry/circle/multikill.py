import sys
input = sys.stdin.readline

def two_circles_meet(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return (x1-x2)**2 + (y1-y2)**2 <= r**2

def meeting_circles(p1):
    res = 0
    for i in range(n):
        if two_circles_meet(p1,coords[i]):
            res += 1
    return res

def two_meet_coords(p1,p2):



t = int(input())
for _ in range(t):
    r,n = map(int,input().split())
    coords = [list(map(int,input().split())) for _ in range(n)]

