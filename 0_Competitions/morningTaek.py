import sys
input = sys.stdin.readline

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
S = set()

for x,y in L:
    if x == 0:
        if y > 0:
            S.add("UP")
        elif y < 0:
            S.add("DOWN")
    elif y == 0:
        if x < 0:
            S.add("LEFT")
        elif x > 0:
            S.add("RIGHT")
    else:
        d = y/x
        S.add(d)

print(len(S))