n,m = map(int,input().split())
l = 1
r = m
j = int(input())

dist = 0
for _ in range(j):
    apple = int(input())

    mv = 0
    if apple > r:
        mv = apple - r
    elif apple < l:
        mv = apple - l
    dist += abs(mv)
    r += mv
    l += mv

print(dist)
