from collections import deque

h,w = map(int,input().split())
L = [list(input()) for _ in range(h)]

open = False
area = 0
for i in range(h):
    for j in range(w):
        if L[i][j] == "/" or L[i][j] == "\\":
            if open:
                area += 1
            open = not open
        else:
            if open:
                area += 1
    open = False
print(area)