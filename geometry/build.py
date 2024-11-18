n = int(input())
s = 0
L = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    x1,y1 = L[i-1]
    x2,y2 = L[i]
    s += abs(x1-x2) + abs(y1-y2)
print(s)