import sys
input = sys.stdin.readline

s,n,m = map(int,input().split())
maxS = s
useS = 0

for _ in range(n+m):
    cmd = int(input())
    if cmd == 0:
        useS -= 1
    elif cmd == 1:
        useS += 1

    if useS > maxS:
        maxS *= 2

print(maxS)
