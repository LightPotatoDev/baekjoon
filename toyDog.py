n,k = map(int,input().split())
moves = input()
trace = []

y,x = 0,0
for m in moves:
    if m == 'U':
        y += 1
    if m == 'D':
        y -= 1
    if m == 'L':
        x -= 1
    if m == 'R':
        x += 1
    trace.append((y,x))

dy,dx = y,x
def pass_origin(y,x,dy,dx):
    def pass_steps(a,da):
        if da == 0 and a != 0:
            return -1
        if da == 0 and a == 0:
            return -2
        if a < 0 and da > 0 and a+da*(k-1) >= 0 and abs(a)%da == 0:
            return abs(a) // da
        if a > 0 and da < 0 and a+da*(k-1) <= 0 and a%abs(da) == 0:
            return a // abs(da)
        return -1

    yStep = pass_steps(y,dy)
    xStep = pass_steps(x,dx)
    if yStep != -1 and xStep != -1 and (yStep == xStep or yStep == -2 or xStep == -2):
        return True
    else:
        return False

ans = "NO"
for i,j in trace:
    if pass_origin(i,j,dy,dx):
        ans = "YES"
        break

print(ans)
