import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    L = [list(map(int,input().split())) for _ in range(n)]

    L.sort()
    best = 100001
    hire = 0
    for i in L:
        if i[1] < best:
            hire += 1
            best = i[1]

    print(hire)
