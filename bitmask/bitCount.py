import sys
input = sys.stdin.readline

table = [[0]*60 for _ in range(60)]
for i in range(60):
    table[i][1] = i+1
    table[i][2] = (i-1)*i // 2
for i in range(1,60):
    for j in range(3,60):
        table[i][j] = table[i-1][j-1] + table[i-1][j]
kValues = [0, 0, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 2, 1, 2, 2, 3, 2, 3, 3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 2, 3, 3, 2, 3, 2, 2, 3, 3, 2, 2, 3]

def addBits(L,i,shift):
    for j in range(shift,60):
        L[j] += table[i][j-shift]
    return L

def bitCounter(n):
    shift = 0
    L = [0]*60
    for i in range(59,-1,-1):
        if ((n >> i) & 1) == 1:
            L = addBits(L,i,shift)
            shift += 1

    return L

while True:
    lo,hi,x = map(int,input().split())
    if lo == 0:
        break

    A = bitCounter(hi)
    B = bitCounter(lo-1)
    L = [0]*11

    for i in range(60):
        L[kValues[i]+1] += A[i]-B[i]
    if (lo == 1):
        L[0] += 1
        L[1] -= 1
    print(L[x])

