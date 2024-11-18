import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
stkI = []
stkD = []

for i,x in enumerate(L):
    if not stkI or stkI[-1][1] <= x:
        stkI.append((i,x))

    while stkD and stkD[-1][1] <= x:
        stkD.pop()
    stkD.append((i,x))

    print(stkI)
    print(stkD)