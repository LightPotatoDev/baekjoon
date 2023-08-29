x1,y1 = map(int,input().split())
n = int(input())

xa,ya = 0,0
closest = 9999
for _ in range(n):
    x2,y2 = map(int,input().split())
    d = abs(x1-x2) + abs(y1-y2)
    if d < closest:
        xa,ya = x2,y2
        closest = d
print(xa,ya)