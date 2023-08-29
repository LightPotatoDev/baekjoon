import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
s = int(input())
maxOk = 0

while s > 0:
    if maxOk == len(L)-1:
        break

    A = L[maxOk:maxOk+s+1]
    maxE = max(A)
    maxI = A.index(maxE)

    if maxI == 0:
        maxOk += 1
        continue

    s -= maxI
    for i in range(maxOk+maxI, maxOk, -1):
        L[i],L[i-1] = L[i-1],L[i]
    maxOk += 1

print(*L)