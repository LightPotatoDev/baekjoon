import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    L = [list(map(int,input().split())) for _ in range(n)]

    best1 = 0
    best2 = 0
    for i in L:
        if i[0] == 1:
            best1 = i
        if i[1] == 1:
            best2 = i

    if best1 == best2:
        print(1)
        continue

    hire = 2
    for s1,s2 in L:
        if s1 < best2[0] and s2 < best1[1]:
            hire += 1

    print(hire)
