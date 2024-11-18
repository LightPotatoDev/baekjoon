import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
x_points = []
last_x = int(1e10) #맨 처음 직선이 아래쪽으로 들어갈 때를 위한 예외처리
num = 0
for i in range(n):
    x,y = points[i]
    nx,ny = points[(i+1)%n]
    if y*ny < 0:
        if num == 0 and y > 0 and ny < 0:
            last_x = nx
            num = 1
        else:
            x_points.append((num//2, nx))
        num += 1
if last_x != int(1e10):
    x_points.append((num//2, last_x))

x_points.sort(key=lambda x:x[1])
stk = []

inc = 0
non_inc = 0
prev_point = -1
for a,_ in x_points:
    stk.append(a)
    if len(stk) >= 2 and stk[-1] == stk[-2]:
        stk.pop()
        stk.pop()
        if prev_point == a:
            non_inc += 1
        if len(stk) == 0:
            inc += 1
    prev_point = a

print(inc, non_inc)